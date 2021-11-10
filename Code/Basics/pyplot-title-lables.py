# With Pyplot, you can use the title() function to set a title for the plot.
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Farm Data")
plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.show()

""" FURTHER INFORMATION 

You can use the fontdict parameter in xlabel(), 
ylabel(), and title() to set font properties for the title and labels.

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Farm Data", fontdict = font1)
plt.xlabel("Latitude", fontdict = font2)
plt.ylabel("Longitude", fontdict = font2)

plt.plot(x, y)

NOTE:
    You can use the loc parameter in title() to position the title.
    Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
"""