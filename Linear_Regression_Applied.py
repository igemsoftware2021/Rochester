from matplotlib import pyplot
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import array

# determining the relationship between Sweat and Plasma Concentration for
# IL-1beta:


# Data for Sweat Concentration of IL-1b eyeballed from graph (source of
# error) in Marques-Deak, A.; Cizza, G.; Eskandari, F.; Torvik, S.;
# Christie, I.C.; Sternberg, E.M.; Philips, T.M. Measurement of cytokines
# in sweat patches and plasma in healthy women: Validation in a controlled
# study. Journal of Immunological Methods. 2006, 315, 99-109. DOI:
# 10.1016/j.jim.2006.07.011
il1bsweat = array([6.9, 6.9, 7, 7.5, 8.4, 10.2, 11.1, 13.5, 18.5])

# Data for Plasma Concentration of IL-1b from graph in Marques-Deak et al.
il1bplasma = array([7.1, 5.9, 5.1, 4.9, 6.3, 9, 7.9, 11.9, 16.2])


# Source: kennytm, 2010. How to do exponential and logarithmic curve
# fitting in Python? I found only polynomial fitting. stack overflow.
# https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# (accessed September 4, 2021).
# This source is about exponential, but the setup works for linear regression.

# We expect Plasma Concentration to vary linearly with Sweat Concentration
# according to Marques-Deak et al.
params, covariance = curve_fit(
    lambda t, a, b: a + b * t, il1bsweat, il1bplasma)

print(f'a and b: {params}')
print(
    f'Equation predicting IL-1beta Concentration in Plasma from Sweat: {params[0]} + {params[1]}x')

font1={'family':'serif','color':'#6ccfe2'}

# Source on how to specify colors: https://matplotlib.org/stable/tutorials/colors/colors.html#sphx-glr-tutorials-colors-colors-py
# Source for hexidecimal code of color: https://www.color-hex.com/color/6ccfe2

# Plots the data points themsevles for IL-1beta from Marques-Deak et al.
pyplot.scatter(il1bsweat, il1bplasma, label='data from Marques-Deak et al.',color='#929292') # Source on formatting matplotlib: https://towardsdatascience.com/all-your-matplotlib-questions-answered-420dd95cb4ff

# Plots the best fit line
plt.plot(il1bsweat, params[0] + params[1] * il1bsweat, label='line of best fit',color='#6ccfe2',linestyle='--');
plt.legend();
plt.ylabel('Plasma Concentration (pg/mL)', fontsize = 10); #for y label
plt.xlabel('Sweat Concentration (pg/mL)', fontsize = 10); #for x label
plt.title('Plasma-Sweat Concentration Relationship for IL-1beta',fontdict=font1,fontsize=15); #source: https://www.w3schools.com/python/matplotlib_labels.asp

# Source: Munir, 2016. Matplotlib plots aren't shown when running file
# from bash terminal. stack overflow.
# https://stackoverflow.com/questions/36269746/matplotlib-plots-arent-shown-when-running-file-from-bash-terminal
# (accessed September 9, 2021).
plt.show()


# determining the relationship between Sweat and Plasma Concentration for IL-6:


# Data for Sweat Concentration of IL-6 eyeballed from graph (source of
# error) in Marques-Deak, A., et al.
il6sweat = array([7.8, 8.2, 8.4, 8.5, 9.5, 10.4, 11.6, 11.7, 14.5])

# Data for Plasma Concentration of IL-6 from graph in Marques-Deak et al.
il6plasma = array([5.1, 10.2, 6.6, 8.2, 7.3, 7.8, 8.8, 10.3, 11.8])


# Source: kennytm, 2010. How to do exponential and logarithmic curve
# fitting in Python? I found only polynomial fitting. stack overflow.
# https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# (accessed September 4, 2021).
# This source is about exponential, but the setup works for linear regression.

# We expect Plasma Concentration to vary linearly with Sweat Concentration
# according to Marques-Deak et al.
params, covariance = curve_fit(
    lambda t, a, b: a + b * t, il6sweat, il6plasma)

print(f'a and b: {params}')
print(
    f'Equation predicting IL-6 Concentration in Plasma from Sweat: {params[0]} + {params[1]}x')

font1={'family':'serif','color':'#6ccfe2'}

# Source on how to specify colors: https://matplotlib.org/stable/tutorials/colors/colors.html#sphx-glr-tutorials-colors-colors-py
# Source for hexidecimal code of color: https://www.color-hex.com/color/6ccfe2

# Plots the data points themsevles for IL-6 from Marques-Deak et al.
pyplot.scatter(il6sweat, il6plasma, label='data from Marques-Deak et al.',color='#929292') # Source on formatting matplotlib: https://towardsdatascience.com/all-your-matplotlib-questions-answered-420dd95cb4ff

# Plots the best fit line
plt.plot(il6sweat, params[0] + params[1] * il6sweat, label='line of best fit',color='#6ccfe2',linestyle='--');
plt.legend();
plt.ylabel('Plasma Concentration (pg/mL)', fontsize = 10); #for y label
plt.xlabel('Sweat Concentration (pg/mL)', fontsize = 10); #for x label
plt.title('Plasma-Sweat Concentration Relationship for IL-6',fontdict=font1,fontsize=15); #source: https://www.w3schools.com/python/matplotlib_labels.asp

# Source: Munir, 2016. Matplotlib plots aren't shown when running file
# from bash terminal. stack overflow.
# https://stackoverflow.com/questions/36269746/matplotlib-plots-arent-shown-when-running-file-from-bash-terminal
# (accessed September 9, 2021).
plt.show()


# determining the relationship between Sweat and Plasma Concentration for
# TNF-alpha:


# Data for Sweat Concentration of TNF-a eyeballed from graph (source of
# error) in Marques-Deak, A., et al.
tnfasweat = array([9.4, 9.9, 10.1, 10.2, 11.8, 12.9, 13.8, 16.6, 20.5])

# Data for Plasma Concentration of TNF-a from graph in Marques-Deak et al.
tnfaplasma = array([5.9, 6.6, 8.1, 8.5, 8.7, 10.2, 11.2, 13.8, 14.8])


# Source: kennytm, 2010. How to do exponential and logarithmic curve
# fitting in Python? I found only polynomial fitting. stack overflow.
# https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# (accessed September 4, 2021).
# This source is about exponential, but the setup works for linear regression.

# We expect Plasma Concentration to vary linearly with Sweat Concentration
# according to Marques-Deak et al.
params, covariance = curve_fit(
    lambda t, a, b: a + b * t, tnfasweat, tnfaplasma)

print(f'a and b: {params}')
# [6.53676471 2.13970588]
print(
    f'Equation predicting TNF-alpha Concentration in Plasma from Sweat: {params[0]} + {params[1]}x')


font1={'family':'serif','color':'#6ccfe2'}

# Source on how to specify colors: https://matplotlib.org/stable/tutorials/colors/colors.html#sphx-glr-tutorials-colors-colors-py
# Source for hexidecimal code of color: https://www.color-hex.com/color/6ccfe2

# Plots the data points themsevles for TNF-alpha from Marques-Deak et al.
pyplot.scatter(tnfasweat, tnfaplasma, label='data from Marques-Deak et al.',color='#929292') # Source on formatting matplotlib: https://towardsdatascience.com/all-your-matplotlib-questions-answered-420dd95cb4ff

# Plots the line of best fit
plt.plot(tnfasweat, params[0] + params[1] * tnfasweat, label='line of best fit',color='#6ccfe2',linestyle='--');
plt.legend();
plt.ylabel('Plasma Concentration (pg/mL)', fontsize = 10); #for y label
plt.xlabel('Sweat Concentration (pg/mL)', fontsize = 10); #for x label
plt.title('Plasma-Sweat Concentration Relationship for TNF-alpha',fontdict=font1,fontsize=15); #source: https://www.w3schools.com/python/matplotlib_labels.asp

# Source: Munir, 2016. Matplotlib plots aren't shown when running file
# from bash terminal. stack overflow.
# https://stackoverflow.com/questions/36269746/matplotlib-plots-arent-shown-when-running-file-from-bash-terminal
# (accessed September 9, 2021).
plt.show()


print('for CRP and Lactoferrin we have to assume 1:1 ratio from sweat to plasma because there is nothing in the literature, which is reasonable given that Marques-Deak 2006 reports ???No significant differences were found between sweat and plasma??? for any cytokines, so it might be a similar story for CRP and Lactoferrin.')
