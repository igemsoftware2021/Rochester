<!--![GitHub contributors](https://img.shields.io/github/contributors/iGEMUoR/Rochester?color=green)-->
<!--![Lines of code](https://img.shields.io/tokei/lines/github/iGEMUoR/Rochester?style=plastic)-->

# Rochester

## Overview

Our Modeling is divided into two sections: answering questions for our wetlab and hardware, or making our actual readout/diagnosis possible. 
Reduction_model_code.txt and v2_flow.m fall into that first camp. The Shewanella Metabolic modeling described on our wiki https://2021.igem.org/Team:Rochester/Model also falls
into this camp, but that modeling was performed in a software known as Cell Collective rather than using code that we could put on GitHub. 

The remaining models make up our pipeline to convert our team's hardware's electrical reading into a predicted concentration in either plasma or serum, two types of blood. Our
software, software (1).ipynb, then compares this predicted concentration to accepted diagnostic cutoffs to provide a yes/no sepsis reading from each biomarker, modular such that the software can be used for any diseases with known biomarker cutoffs.

We have committed several iterations of many of our models as we have improved them, but please read the most recent versions for the most thorough documentation when looking to understand how our models work!

### Overview of each model

See our team's wiki page for background and definitions for the relevant model: https://2021.igem.org/Team:Rochester/Model
  
See the documentation in the code and the relevant writeups on the wiki above for explanations of tecnnical detail.

#### Reduction Method Model
  
This model predicts how many and what type of functional groups remain on the rGO, depending on the degree of reduction. This is to inform what concentrations of aptamers should be used for optimal attachment.

#### Fluid flow and binding/dissocation
  
It is important to figure out time at which  binding and dissociation of biomarkers occurs, so that the concentration that sensor effectively sees reflects the concentration in the new sweat. This will aid the hardware team with figuring out the dimensions for various channels in the microfluidic device. This way, the dimensions could be altered in COMSOL and the new simulation of the fluid flow can give us the velocity of the fluid.

#### Pipeline
  
Our pipeline for producing a diagnostic readout from the electrical signal measured by our hardware consists of curve_fitting_experimentation.ipynb, Exponential_Regression_Framework.py, Linear_Regression_Framework.py, and Linear_Regression_Applied.py. The first 3 models were all more rough and done along the way, which you can see for our debugging and learning-the-necessary code process. In Linear_Regression_Applied.py, we actually determine the parameters in the equations to convert sweat concentration to plasma concentration. As of October 13th we have not yet been able to apply the Exponential_Regression_Framework.py to determine parameters for the earlier-in-the-pipeline conversion of Resistance (the electrical property) to sweat concentration because we are awaiting calibration data from experiments. Our final software that converts the input Resistance value into an upvote-downovte for each biomarke is software (1).ipynb.
  
### Prerequisites and Installation for each model 
  
#### Reduction Method Model
  
Prerequisites: R and (recommended) R Studio for Linux, Windows, or MacOS. See https://techvidvan.com/tutorials/install-r/ for instructions for all operating systems. 
  
To run from the command line: https://support.rstudio.com/hc/en-us/articles/218012917-How-to-run-R-scripts-from-the-command-line
Prerequisite: for Linux users
  
#### Fluid flow and binding/dissocation

Prerequisites: MATLAB, and therefore a Mathworks account and license. Common for universities to have licenses. Instructions here: https://www.mathworks.com/help/install/ug/install-products-with-internet-connection.html 

#### Pipeline
  
Installation
  
Prerequisites: Python https://www.python.org/downloads/ and use built-in PIP https://realpython.com/what-is-pip/#installing-packages-with-pip to install the NumPy https://numpy.org/install/, SciPy https://www.scipy.org/install.html#pip-install, and matplotlib https://matplotlib.org/stable/users/installing.html packages; Jupyter (for curve_fitting_experimentation.ipynb). Can run files from command line but graphical display is more user friendly in Jupyter notebook. 

