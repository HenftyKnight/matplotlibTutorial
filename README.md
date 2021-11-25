# matplotlibTutorial

Table of Contents
Introduction
Simple Plot
Figures, Subplots, Axes and Ticks
Animation
Other Types of Plots
Beyond this Tutorial
References


<h1> Introduction </h1>
Matplotlib is a multiplatform data visualization library built on NumPy arrays, and
designed to work with the broader SciPy stack. It was conceived by John Hunter in
2002, originally as a patch to IPython for enabling interactive MATLAB-style plotting via gnuplot from the IPython command line.

matplotlib is probably the single most used Python package for 2D-graphics. It provides both a very quick way to visualize data from Python and publication-quality figures in many formats.

Where is the Matplotlib Codebase?
The source code for Matplotlib is located at this github repository 
(https://github.com/matplotlib/matplotlib)

<h2> pyplot </h2>
matplotlib.pyplot is a collection of command style functions that make Matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.
pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation.

```python
from matplotlib import pyplot as plt
```

<h2> IPython </h2>

IPython is an enhanced interactive Python shell that has lots of interesting features including named inputs and outputs, access to shell commands, improved debugging and much more. It allows interactive matplotlib sessions that have Matlab/Mathematica-like functionality.

<h1> The Matplotlib Object Hierarchy </h1>
If you’ve worked through any introductory matplotlib tutorial, you’ve probably called something like plt.plot([1, 2, 3]). This one-liner hides the fact that a plot is really a hierarchy of nested Python objects. A “hierarchy” here means that there is a tree-like structure of matplotlib objects underlying each plot.

A Figure object is the outermost container for a matplotlib graphic, which can contain multiple Axes objects. One source of confusion is the name: an Axes actually translates into what we think of as an individual plot or graph (rather than the plural of “axis,” as we might expect).

You can think of the Figure object as a box-like container holding one or more Axes (actual plots). Below the Axes in the hierarchy are smaller objects such as tick marks, individual lines, legends, and text boxes. Almost every “element” of a chart is its own manipulable Python object, all the way down to the ticks and labels:

![alt-text](https://files.realpython.com/media/fig_map.bc8c7cabd823.png "TREE HIERARCHY")


```python
>>> fig, _ = plt.subplots()
>>> type(fig)
<class 'matplotlib.figure.Figure'>
```

Above, we created two variables with plt.subplots(). The first is a top-level Figure object. The second is a “throwaway” variable that we don’t need just yet, denoted with an underscore.

Matplotlib presents this as a figure anatomy, rather than an explicit hierarchy:

![alt-text](https://files.realpython.com/media/anatomy.7d033ebbfbc8.png "MATPLOTLIB FIGURE ANATOMY")