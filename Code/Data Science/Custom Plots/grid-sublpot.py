# Aligned columns or rows of subplots are a common-enoug
# need that Matplotlib has several convenience routines 
# that make them easy to create. The lowest level of these
# is plt.subplot(), which creates a single subplot within 
# grid. As you can see, this command takes three integer 
# arguments—the number of rows, the number of columns, and 
# the index of the plot to be created in this scheme, which
# runs from the upper left to the bottom right:

import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')


# Adjusted Spacing
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)),
           fontsize=18, ha='center')

plt.show()