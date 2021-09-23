# Rochester

Overview

Our Modeling falls into two results-focused/goal-oriented camps: answering questions for our wetlab and hardware, or making our actual readout/diagnosis possible. 
Reduction_model_code.txt and v2_flow.m fall into that first camp, and the remaining models make up our pipeline to convert our team's hardware's electrical reading into a predicted concentration in either plasma or serum, two types of blood. The Shewanella Metabolic modeling described on our wiki https://2021.igem.org/Team:Rochester/Model also falls into this camp, but that modeling was performed in a software known as Cell Collective rather than using code that we could put on GitHub. 

In an effort to make use of GitHub's wonderful version-control enabling, we have committed several iterations of many of our models as we have improved them, but please read the most recent versions for the most thorough documentation when looking to understand how our models work!

**Overview of each model

*Reduction Method Model

*Fluid flow and binding/dissocation

*Pipeline
  
Our pipeline for producing a diagnostic readout from the electrical signal measured by our hardware consists of curve_fitting_experimentation.ipynb, Exponential_Regression_Framework.py, Linear_Regression_Framework.py, and Linear_Regression_Applied.py. The first 3 models were all more rough and done along the way, with our final software that converts the input Resistance value into an upvote-downovte for each biomarker being <filename>.
