"""
    Plotting the Latitude vs Longitude coordinates of the Plants 
    and visualizing it through matplotlib
"""
import matplotlib.pyplot as plt
import pandas as pd

T1 = "Additional Data\Data\T1_Data_VineScout2020_Zenodo.csv"
read_t1 = pd.read_csv(T1)
plants=pd.DataFrame(read_t1)
print(plants)

ax = plt.gca()
plants.plot(kind='line',x='Lat',y='Lon',ax=ax,label='Lat Vs. Lon')
ax.set_ylabel("Longitude Values")
ax.set_xlabel("Latitude Values")
plt.title('Demo graph For Line Plots')
plt.show()