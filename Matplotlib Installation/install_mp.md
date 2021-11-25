# How to install matplotlib?

At first make sure you have pip or some other pre-built packages installed!

pip works on Unix/Linux, OS X, and Windows.
pip comes with Python (no need to install it seperately)

**Install Latest Version PIP**    
[pip](https://pypi.org/project/pip/)

**Source install from git**

When you are interested in contributing to matplotlib development, running the latest source code, or just like to build everything yourself, it is not dicult to build matplotlib from source:

```
>>> git clone git@github.com:matplotlib/matplotlib.git
>>> cd matplotlib
>>> python setup.py build
>>> python setup.py install
```

**Mac OS**
    new terminal APP
```
curl -O https://bootstrap.pypa.io/get-pip.py python get-pip.py pip install matplotlib
```

If you want to install IPython with the dependencies needed for Ipython notebooks

```
pip install ipython[notebook]
```
**Linux**

    Use the package manager of your choice:
        
        Fedora / Redhat:
            sudo yum install python-matplotlib
        Debian / Ubuntu:
            sudo apt-get install python-matplotlib
        Arch:
            sudo pacman -S python-matplotlib
    
    Usually the package should be called something like python-pip

**Windows**

Install Python -> 
[python release](https://www.python.org/downloads/windows/) 

    Use one of the scipy-stack compatible Python distributions such as Python(x,y), Enthought Canopy, or Continuum Anaconda.

    Install the latest (python 3.4+ includes pip)

    Add pip to your PATH by adding the Scripts/ subdirectory of your python installation to this environment variable:

    Start → Control Panel → System → Advanced → Environment Variables ...
    
    Append Path under System Variables with the Path of the Scripts directory, the default is C:\Python(x,y)\Scripts

**install matplotlib**

    Sidenote: 
        If you haven't installed Ipython yet, then you can install it via pip install ipython[notebook] (installs with dependencies for Ipython notebooks)

    pip install matplotlib
    or 
    use the precompiled installers for installing matplotlib, which is recommended
**Precompiled Installer for matplotlib**

[matplotlib](https://matplotlib.org/stable/)

**check your installation**

```
python3 -c 'import matplotlib; print(matplotlib.__version__, matplotlib.__file__)'

python2.7 -c 'import matplotlib; print(matplotlib.__version__, matplotlib.__file__)'

```