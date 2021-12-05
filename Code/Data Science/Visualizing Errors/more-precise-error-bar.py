# In addition to these basic options, the 
# errorbar function has many options to fine-tune the outputs.
#  Using these additional options you can easily customize 
# the aesthetics of your errorbar plot. I often find it helpful,
#  especially in crowded plots, to make the errorbars lighter 
# than the points themselves:

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np



x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0)

plt.show()

# In addition to these options, you can also specify horizontal
#  errorbars (xerr), one-sided errorbars, and many other variants.
#  For more information on the options available, refer to the 
# docstring of plt.errorbar.