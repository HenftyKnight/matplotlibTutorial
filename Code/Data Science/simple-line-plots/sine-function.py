import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
ax = plt.axes() 

x = np.linspace(0, 10, 1000)
# An Interesting to note here we are using the PYLAB
# let the figure and axes be created for us in the background 
ax.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()