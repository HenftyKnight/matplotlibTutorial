import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np



x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

# Here the fmt is a format code controlling 
# the appearance of lines and points, and has the
#  same syntax as the shorthand used in plt.plot
plt.errorbar(x, y, yerr=dy, fmt='.k')
plt.show()