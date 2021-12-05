import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
ax = plt.axes() 

x = np.linspace(0, 10, 1000)
# Matplotlib does a decent job of choosing 
# default axes limits for your plot, but sometimes 
# it's nice to have finer control. The most basic way 
# to adjust axis limits is to use the 
# plt.xlim() and plt.ylim() methods:
plt.plot(x, np.sin(x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# -----------------------------------------------
# If for some reason you'd like either axis to 
# be displayed in reverse, you can simply reverse the order of the arguments:
plt.plot(x, np.sin(x))

plt.xlim(10, 0)
plt.ylim(1.2, -1.2)
# -------------------------------------------------

# -------------------------------------------------
# A useful related method is plt.axis() 
# (note here the potential confusion between axes with an e, and axis with an i).
#  The plt.axis() method allows you to set the x and y limits with a single call,
#  by passing a list which specifies [xmin, xmax, ymin, ymax]:


plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5]);

# --------------------------------------------------------------


#----------------------------------------------------------
# The plt.axis() method goes even beyond this, allowing you to do things
# like automatically tighten the bounds around the current plot:

plt.plot(x, np.sin(x))
plt.axis('tight')

#----------------------------------------------------------

#----------------------------------------------------------
# It allows even higher-level specifications, such as ensuring an 
# equal aspect ratio so that on your screen, one unit in x is equal to one unit in y:
plt.plot(x, np.sin(x))
plt.axis('equal')
#----------------------------------------------------------