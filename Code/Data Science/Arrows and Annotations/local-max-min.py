import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('classic')
import numpy as np
fig, ax = plt.subplots()

x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')

ax.annotate('local minimum', xy=(5 * np.pi, -1), xytext=(2, -6),
            arrowprops=dict(arrowstyle="-",facecolor='black',
                            connectionstyle="angle3,angleA=0,angleB=-90"))
ax.annotate('local maximum', xy=(6.28, 1), xytext=(10, 4),
            arrowprops=dict(facecolor='red', shrink=0.05))

plt.show()