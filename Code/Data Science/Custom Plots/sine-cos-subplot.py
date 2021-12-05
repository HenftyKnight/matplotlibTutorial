import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

fig = plt.figure()

# These numbers represent [left, bottom, width, height] 
# in the figure coordinate system, which ranges from 0.1 
# at the bottom left of the figure to 0.5 at the top right
# of the figure.

ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                   xticklabels=[], ylim=(-1.2, 1.2))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                   ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x))

plt.show()