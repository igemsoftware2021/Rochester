# Source on numpy data types: Johnson, J. Python Numpy Tutorial (with
# Jupyter and Colab). CS231n Convolutional Neural Networks for Visual
# Recognition. https://cs231n.github.io/python-numpy-tutorial/ (accessed
# September 4, 2021).

from matplotlib import pyplot
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import array


# Dummy data for x, Sweat Concentration we're converting to Plasma Concentration (generated by hand, which is not standard
# procedure. See wiki writeup):
xdata = array([5, 10, 15, 20, 25, 30, 35, 40, 45,
              50, 55, 60, 65, 70, 75, 80, 85])

# Corresponding dummy data for y, Plasma Concentration (same procedure):
ydata = array([1, 20, 39, 60, 76, 91, 103, 101, 100,
              102, 108, 106, 120, 151, 160, 180, 230])


# Source: kennytm, 2010. How to do exponential and logarithmic curve
# fitting in Python? I found only polynomial fitting. stack overflow.
# https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# (accessed September 4, 2021).
# This source is about exponential, but the setup works for linear regression.

# We expect Plasma Concentration to vary linearly with Sweat Concentration.
# Source: Marques-Deak, A.; Cizza, G.; Eskandari, F.; Torvik, S.;
# Christie, I.C.; Sternberg, E.M.; Philips, T.M. Measurement of cytokines
# in sweat patches and plasma in healthy women: Validation in a controlled
# study. Journal of Immunological Methods. 2006, 315, 99-109. DOI:
# 10.1016/j.jim.2006.07.011
params, covariance = curve_fit(
    lambda t, a, b: a + b * t, xdata, ydata)

print(f'a and b: {params}')
# [6.53676471 2.13970588]
print(
    f'Equation predicting Plasma Concentration from Sweat Concentration: {params[0]} + {params[1]}x')

# Poor fit because this dummy data is not very linear, but the
# real experimental data we collect likely will be.

# Plots the dummy data points themsevles 
pyplot.scatter(xdata, ydata, label='dummy data',color='#929292') # Source on formatting matplotlib: https://towardsdatascience.com/all-your-matplotlib-questions-answered-420dd95cb4ff

font1={'family':'serif','color':'#6ccfe2'}

# Plots the line of best fit
plt.plot(xdata, params[0] + params[1] * xdata, label='line of best fit',color='#6ccfe2',linestyle='--');
plt.legend();
plt.ylabel('Plasma Concentration (units)', fontsize = 10); #for y label
plt.xlabel('Sweat Concentration (units)', fontsize = 10); #for x label
plt.title('Plasma-Sweat Concentration Relationship for Dummy Data',fontdict=font1,fontsize=15); #source: https://www.w3schools.com/python/matplotlib_labels.asp

# Source: Munir, 2016. Matplotlib plots aren't shown when running file
# from bash terminal. stack overflow.
# https://stackoverflow.com/questions/36269746/matplotlib-plots-arent-shown-when-running-file-from-bash-terminal
# (accessed September 9, 2021).
plt.show()