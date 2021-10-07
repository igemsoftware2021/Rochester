%kinetic parameters for normal levels of CRP. CRP chosen because it had the
%lowest kd 
kd_CRP = 6.2E-12; %Kd of CRP in M
c_CRP = 6.6E-8;%normal concentration of CRP in M
fracbound_eq=c_CRP/(c_CRP+kd_CRP); %fraction bound of CRP at equilibrium
kon_CRP = [10^5:20e4:10^6]; %range of kon rates for CRP in 1/Ms based on literature 
kobs_on_CRP= c_CRP*kon_CRP; %1/s
t= 0:1:100; %s 
fracbound_t=[];


for i=1:length(kon_CRP)
    fracbound_t=fracbound_eq*(1-exp(-kobs_on_CRP(i).*t)); %fraction bound as a function of time and concentration 
    plot (t,fracbound_t)
    hold on 
end


% microfluidic parameters

length_microfluidics = 169; % units mm
width_microfluidics = 30.5; % units mm
thickness_microfluidics = 5; % units mm

vol=length_microfluidics*10^-3*width_microfluidics*10^-3*...
    thickness_microfluidics*10^-3;
time_to_half= 12; %s from plot 
flowrate=vol/time_to_half; %m3/s



% need to solve for U (flow rate) based on dissociation/binding.
% incorporate Navier Stokes, boundary and initial conditions
%aptamer=B, biomarker=A

%% Practice Navier Stokes 
%% Boundary and Mesh Parameters
length_microfluidics = 169E-3; %length along the positive x-directon of the flow domain (in mm, mictofluidic length)
breadth = 30.5E-3;%length along the positive y-direction of the flow domain (width in mm)
mesh_x = 50; %number of cells discretized along the x-direction 
mesh_y = 20; %number of cells discretized along the y-direction
dx = length_microfluidics/mesh_x; %cell size along the x-direction
dy = breadth/mesh_y; %cell size along the y-direction

% fluid properties
mu = 0.0012; %viscosity of the fluid Pa s 
rho = 997; %density of the fluid in kg/m^3



%iteration parameters and relaxation factors
omega_u = 0.7; %relaxation parameter for u momentum 
omega_v = 0.7; %relaxation parameter for v momentum
omega_p = 0.3; %relaxation parameter for pressure correction
outer_iterations = 100; %number of times SIMPLE is going to be iterated through for convergence
iter_v = 10; %number of iterations for u and v momentum solvers
iter_p = 100; %number of iterations for pressure correction solver

%% Flow variables
u = zeros(mesh_y+2,mesh_x+1);%u momentum
v = zeros(mesh_y+1,mesh_x+2);%v momentum
u_old = zeros(mesh_y+2,mesh_x+1); %guessed x-momentum on the cell centers
v_old = zeros(mesh_y+1,mesh_x+2); %guessed y-momentum on the cell centers
p_prime = zeros(mesh_y+2,mesh_x+2); %pressure correction
pressure = zeros(mesh_y+2,mesh_x+2);%pressure term
apu = ones(mesh_y+2,mesh_x+2);%coefficient of p-term in u momentum
apv = ones(mesh_y+2,mesh_x+2);%coefficient of p-term in v momentum
app = ones(mesh_y+2,mesh_x+2);%coefficient of p-term for pressure corrections
ae = zeros(mesh_y+2,mesh_x+2);%east coefficient for velocities
as = zeros(mesh_y+2,mesh_x+2);%south coefficient for velocities
an = zeros(mesh_y+2,mesh_x+2);%north coefficient for velocities
aw = zeros(mesh_y+2,mesh_x+2);%west coefficient for velocities
source = zeros(mesh_y+2,mesh_x+2); %source term at each stage to check mass conservation

%% BOUNDARY CONDITION SUBROUTINE %%
%choose the appropriate problem and comment/uncomment the suggested lines
%as you scroll down before you hit the run button


%%  Pressure-driven Channel flow 
u(mesh_y+2,:) = 0; %north boundary is the pipe wall
u(1,:)=0; %south boundary is also the pipe wall
u(:,1)=flowrate/(width_microfluidics*10^-3*thickness_microfluidics*10^-3); %inlet velocity specified m/s
% pressure(:,mesh_x+1)=0; %fix outlet pressure
%% Solver using SIMPLE-algorithm
u_old = u;
v_old = v;tot=[];counter=[];residual_u=[];residual_v=[];
%Main outer loop
for k = 1:outer_iterations
    %% X-Momentum subroutine
    %initialize coefficients for the u-momentum the centers 
    for j = 2:mesh_x
        for i=2:mesh_y+1
            ae(i,j) = max(-0.5*rho*dy*(u_old(i,j)+u_old(i,j+1)),0) + mu*dy/dx;
            aw(i,j) = max(0.5*rho*dy*(u_old(i,j)+u_old(i,j-1)),0) + mu*dy/dx;
            an(i,j) = max(-0.5*rho*dx*(v_old(i,j)+v_old(i,j+1)),0) + mu*dx/dy;
            as(i,j) = max(0.5*rho*dx*(v_old(i-1,j)+v_old(i-1,j+1)),0) + mu*dx/dy;
        end
    end
    %correct the boundary values on the north and south boundary for the
    %X-momentum
    for j=2:mesh_x
        an(mesh_y+1,j) = max(-0.5*rho*dx*(v_old(mesh_y+1,j)+v_old(mesh_y+1,j+1)),0) + mu*dx/(dy/2);
        as(2,j) = max(0.5*rho*dx*(v_old(1,j)+v_old(1,j+1)),0) + mu*dx/(dy/2);
    end
    apu = ae+aw+as+an;
     %%%to block out cells%%%
    apu(1:12,20:21) = 1e30;
    apu = apu/omega_u;
    %iterate on the x-momentum equations
    for var = 1:iter_v
        for j = 2:mesh_x
            for i = 2:mesh_y+1
                u(i,j) = (1-omega_u)*u_old(i,j) + (1/apu(i,j))*...
                    (ae(i,j)*u(i,j+1) + aw(i,j)*u(i,j-1) + an(i,j)*u(i+1,j)+ as(i,j)*u(i-1,j) + dy*(pressure(i,j)-pressure(i,j+1)));
            end
        end
        %uncomment this for fully developed flow
        u(:,mesh_x+1) = u(:,mesh_x); %du/dx=0 boundary condition at the exit
    end
    %Uncomment only for CASE 1 (fully developed channel flow)
    %ensure mass conservation each time for the exit
    in_mass_flow = rho*flowrate;; %as declared
    out_mass_flow =0;
    for i = 2:mesh_y
        out_mass_flow = out_mass_flow+ rho*dy*u(i,mesh_x+1);
    end
    u(:,mesh_x+1) = u(:,mesh_x+1)*in_mass_flow/out_mass_flow;
    u(:,1) = u(:,mesh_x+1);%generate fully developed flow




end 

flowrateout= out_mass_flow/rho; %m3/s
