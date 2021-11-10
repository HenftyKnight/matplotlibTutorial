# With Pyplot, you can use the title() function to set a title for the plot.
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Farm Data")
plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.plot(x, y)
plt.grid()
plt.show()

""" Specify Which Grid Lines to Display """
"""

You can use the axis parameter in the grid() 
function to specify which grid lines to display.
Legal values are: 'x', 'y', and 'both'. Default value is 'both'.

plt.grid(axis='x')

------ Set Line Properties for the Grid ------
You can also set the line properties of the grid, 
like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
"""