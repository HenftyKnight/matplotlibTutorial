# You can use the keyword argument linestyle,
# or shorter ls, to change the style of the plotted line:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

""" FURTHER REFERENCES """
# Use a dashed line:
# plt.plot(ypoints, linestyle = 'dashed')

"""
Shorter Syntax
The line style can be written in a shorter syntax:

--> linestyle can be written as ls.
--> dotted can be written as :.
--> dashed can be written as --.

Line Styles
Style 	            Or
'solid' (default) 	'-' 	
'dotted' 	        ':' 	
'dashed' 	        '--' 	
'dashdot' 	        '-.' 	
'None' 	            '' or ' '

"""