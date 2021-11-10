"""
    Display Multiple Plots
    With the subplots() function you can draw multiple plots in one figure:

    Subplots mean groups of axes that can exist in a single matplotlib figure.
    Subplots mean a group of smaller axes (where each axis is a plot)
    that can exist together within a single figure.

    plt.subplot() -> *args int, (int, int, index) or default (1,1,1)
    Three integers (nrows, ncols, index). The subplot will take the 
    index position on a grid with nrows rows and ncols columns. index 
    starts at 1 in the upper left corner and increases to the right. 
    index can also be a two-tuple specifying the (first, last) indices 
    (1-based, and including last) of the subplot,
"""

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

#the figure has 1 row, 2 columns, and this plot is the first plot.
plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

#the figure has 1 row, 2 columns, and this plot is the second plot. 
plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()