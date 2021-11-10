Table of Contents
Introduction
Simple Plot
Figures, Subplots, Axes and Ticks
Animation
Other Types of Plots
Beyond this Tutorial
References

**<h1> Introduction </h1>**
Matplotlib is a multiplatform data visualization library built on NumPy arrays, and
designed to work with the broader SciPy stack. It was conceived by John Hunter in
2002, originally as a patch to IPython for enabling interactive MATLAB-style plotting via gnuplot from the IPython command line.

matplotlib is probably the single most used Python package for 2D-graphics. It provides both a very quick way to visualize data from Python and publication-quality figures in many formats.

Where is the Matplotlib Codebase?
The source code for Matplotlib is located at this github repository 
(https://github.com/matplotlib/matplotlib)

If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.

```python
>>> pip install matplotlib 
```

**<h1> PYPLOT </h2>**
Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

```python
import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array([1,5])
ypoints = np.array([0,100])

plt.plot(xpoints,ypoints)
plt.show()
```
The plot() function is used to draw points (markers) in a diagram.
**todo: SHOW RESULT**

*Plotting Without Line*
To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.