# Source on numpy data types: Johnson, J. Python Numpy Tutorial (with
# Jupyter and Colab). CS231n Convolutional Neural Networks for Visual
# Recognition. https://cs231n.github.io/python-numpy-tutorial/ (accessed
# September 4, 2021).

# Source:
# https://www.geeksforgeeks.org/plot-mathematical-expressions-in-python-using-matplotlib/
from numpy import linspace
from matplotlib import pyplot
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import array
# We expect Concentration to vary with the exponential of Resistance.
# Source: Cai, H.; Lee T.M.; Hsing, I. Label-free protein recognition
# using an aptamer-based impedance measurement assay. Sensors and
# Actuators B: Chemical. 2006, 114, 433-437.
from numpy import exp

# Resistance data for CRP measured with a multimeter
xdata = array([294, 433, 279, 461, 364, 970, 435,
              838, 730, 745, 745, 345, 830, 1300])

#
ydata = array([0,
               1.6,
               3.13,
               6.25,
               7.8,
               12.5,
               15.63,
               25,
               62.5,
               125,
               250,
               500,
               800,
               1000])  # corresponding Sweat Concentration data for CRP


# Source: kennytm, 2010. How to do exponential and logarithmic curve
# fitting in Python? I found only polynomial fitting. stack overflow.
# https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# (accessed September 4, 2021).

# a, b, c, and d are parameters (constants) to be determined, t is
# Resistance, and a + b*log(t) is Concentration
# p0 is our initial guesses for a, b, c, and d, respectively.
# We don't use covariance, just storing it because curve_fit yields two
# outputs.
params, covariance = curve_fit(
    lambda t, a, b, c, d: a + b * exp(c * t + d), xdata, ydata, p0=(0, 1, (1 / 700), 30))

print(f'a, b, c, and d: {params}')

print(
    f'Equation predicting CRP Sweat Concentration (y) from Resistance (x): {params[0]} + {params[1]}e^({params[2]}x + {params[3]})')

# Allows for the graphing of the determined equation as a smooth curve
xdata_displayed = linspace(200, 1500, 100) # creates 100 data points of Resistance evenly spaced from 200 Ohms to 1500 Ohms


# Source on how to specify colors: https://matplotlib.org/stable/tutorials/colors/colors.html#sphx-glr-tutorials-colors-colors-py
# Source for hexidecimal code of color: https://www.color-hex.com/color/6ccfe2
# Source on formatting matplotlib:
# https://towardsdatascience.com/all-your-matplotlib-questions-answered-420dd95cb4ff
font1 = {'family': 'serif', 'color': '#6ccfe2'}

# Graphs the experimental data points themselves
pyplot.scatter(xdata, ydata, label='dummy data', color='#929292')

# Graphs the determined equation as a smooth curve
plt.plot(xdata_displayed,
         params[0] + params[1] * exp(params[2] * xdata_displayed + params[3]),
         label='best fit curve',
         color='#6ccfe2',
         linestyle='--')
plt.legend()
plt.ylabel('Sweat Concentration (nM)', fontsize=10)  # for y label
plt.xlabel('Resistance (Ohms)', fontsize=10)  # for x label
plt.title(
    'Electrical to Concentration Relationship on Experimental Data',
    fontdict=font1,
    fontsize=15)  # source: https://www.w3schools.com/python/matplotlib_labels.asp


# Source: Munir, 2016. Matplotlib plots aren't shown when running file
# from bash terminal. stack overflow.
# https://stackoverflow.com/questions/36269746/matplotlib-plots-arent-shown-when-running-file-from-bash-terminal
# (accessed September 9, 2021).
plt.show()
