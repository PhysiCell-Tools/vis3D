# This directory contains a modified version of the scipy.io module  
[https://projects.scipy.org/scipylib/license.html]

It allows ParaView to load PhysiCell .mat files (which are currently MATLAB v4 binary format).

When you start ParaView, you need to access its Python Shell (View menu) and modify the `sys.path` so it will be able to import the relevant module, i.e., add the path to wherever you saved these files:
```
>>> 
Python 3.9.13 (main, Sep 22 2023, 15:13:28) 
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
>>> from paraview.simple import *
>>> sys.path.append("/Users/heiland/git/vis3D/ParaView/matv4_loader")
>>> 
```


