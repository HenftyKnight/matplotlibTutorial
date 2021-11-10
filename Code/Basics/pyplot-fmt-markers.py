# You can use also use the shortcut string
# notation parameter to specify the marker.
# This parameter is also called fmt, and 
# is written with this syntax:
# marker|line|color

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')

"""
Different Scenarios and additional args used in plt.plot()
Just uncomment each line and checkout the different scenarios
"""
# If you want to set specific size of markers, uncomment below
# plt.plot(ypoints, marker = 'o', ms = 20)

# You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')

# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')

# Use both the mec and mfc arguments to color of the entire marker:
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')

# You can also use Hexadecimal color values:
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

plt.show()

# NOTE: If you leave out the line value in the fmt parameter, no line will be plotted.
""" FURTHER EXTENSION ON DIFFERENT MARKERS AND COLORS"""
"""
Line Syntax 	Description
'-' 	        Solid line 	
':' 	        Dotted line 	
'--' 	        Dashed line 	
'-.' 	        Dashed/dotted line
"""

"""
Color Syntax 	Description
'r' 	        Red 	
'g' 	        Green 	
'b' 	        Blue 	        
'c' 	        Cyan 	        
'm' 	        Magenta 	        
'y' 	        Yellow 	        
'k' 	        Black 	        
'w' 	        White

"""