
# Sometimes when designing a plot you'd like to add multiple legends 
# to the same axes. Unfortunately, Matplotlib does not make this easy:
#  via the standard legend interface, it is only possible to create a 
# single legend for the entire plot. If you try to create a second 
# legend using plt.legend() or ax.legend(), it will simply override 
# the first one. We can work around this by creating a new legend artist 
# from scratch, and then using the lower-level ax.add_artist() method to
#  manually add the second artist to the plot:
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
fig, ax = plt.subplots()

lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)

for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2),
                     styles[i], color='black')
ax.axis('equal')

# specify the lines and labels of the first legend
ax.legend(lines[:2], ['line A', 'line B'],
          loc='upper right', frameon=False)

# Create the second legend and add the artist manually.
from matplotlib.legend import Legend
leg = Legend(ax, lines[2:], ['line C', 'line D'],
             loc='lower right', frameon=False)
ax.add_artist(leg)

plt.show()