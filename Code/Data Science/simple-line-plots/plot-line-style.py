import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()
ax = plt.axes() 

x = np.linspace(0, 10, 1000)

plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted




# If you would like to be extremely terse, 
# these linestyle and color codes can be combined
#  into a single non-keyword argument to the plt.plot() function:

plt.plot(x, x + 8, '-g')  # solid green
plt.plot(x, x + 9, '--c') # dashed cyan
plt.plot(x, x + 10, '-.k') # dashdot black
plt.plot(x, x + 11, ':r');  # dotted red



plt.show()

