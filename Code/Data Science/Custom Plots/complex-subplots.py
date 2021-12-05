import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

# To go beyond a regular grid to subplots that span multiple 
# rows and columns, plt.GridSpec() is the best tool. 
# The plt.GridSpec() object does not create a plot by 
# itself; it is simply a convenient interface that is 
# recognized by the plt.subplot() command. For example,
# a gridspec for a grid of two rows and three columns with some
# specified width and height space looks like this:


grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)

# From this we can specify subplot locations and extents using 
# the familiary Python slicing syntax:
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])

plt.show()