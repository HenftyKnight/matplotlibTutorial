import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()

# # Default Position
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend()

#---------------- Upper Left Legend-------------
ax.legend(loc='upper left', frameon=False)

#-----------------------------------------------
# We can use the ncol command to specify the number of columns in the legend:
ax.legend(frameon=False, loc='lower center', ncol=2)

# # We can use a rounded box (fancybox) or add a shadow, change the transparency
# # (alpha value) of the frame, or change the padding around the text
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)

plt.show()