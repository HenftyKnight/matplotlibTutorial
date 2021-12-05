Fonts for you matplotlib graph

[fonts](https://www.fontsquirrel.com/fonts/list/popular)


Using the fonts in Matplotlib
Once the fonts are installed, you must rebuild the font cache so that it will be available to matplotlib when you make your figure. 
```python
import matplotlib.font_manager as fm # Rebuild the matplotlib font cache
fm._rebuild()
```

Since scientific instrument data is typically fairly simple (usually just one independent variable that we control and a measured, dependent variable), we can use numpy.loadtxt to import our data. For more complicated datasets, I highly recommend using pandas , which has incredibly sophisticated functions for loading and sanitizing data for visualizations — a comprehensive documentation can be found on 
[pandas](https://pandas.pydata.org/pandas-docs/stable/reference/io.html).

[Matplot Lib Cheatsheets](https://matplotlib.org/cheatsheets/)

[Dash Plotly](https://dash.plotly.com/)

Dash is the original low-code framework for rapidly building data apps in Python, R, Julia, and F# (experimental).

Dash is React for Python.