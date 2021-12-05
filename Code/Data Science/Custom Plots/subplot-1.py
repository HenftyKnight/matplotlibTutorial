import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

ax1 = plt.axes()  # standard axes
#These numbers represent [left, bottom, width, height] 
# in the figure coordinate system, which ranges from 0 
# at the bottom left of the figure to 1 at the top right
# of the figure.

# For example, we might create an inset axes at the 
# top-right corner of another axes by setting the x and y
# position to 0.65 (that is, starting at 65% of the width
# and 65% of the height of the figure) and the x and y extents
# to 0.2 (that is, the size of the axes is 20% of the width and
# 20% of the height of the figure):

ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])


plt.show()