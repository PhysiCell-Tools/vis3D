## ParaView to visualize PhysiCell 3D data

ParaView is an open-source, multi-platform data analysis and visualization application. Users create a pipeline to read data, apply filters, and render results. For PhysiCell data, we provide sample pipelines that contain a custom data reader and relevant filters (in an editable Python script).

This README serves as an updated version of an earlier [blog post](http://www.mathcancer.org/blog/paraview-for-physicell-part-1/), but much of the information there is still relevant.

Dependencies:

* We recommend using the [Anaconda Python distribution](https://www.anaconda.com/products/distribution). The current (Oct 2023) version provides Python 3.11.x 

* Download [ParaView](https://www.anaconda.com/products/distribution). The current (Oct 2023) version is 5.11.2 (and it happens to use Python 3.9.11. NOTE: if you want to use any 3rd party Python modules in your ParaView session, it is *required* that your Python "major.minor" version (above) matches that being used by ParaView. So in this case, it would be problematic: 3.11 vs. 3.9)

Usage:

Optionally, as discussed in the blog post, you can specify where your 3D PhysiCell data is located via:
```
export PHYSICELL_DATA=full-path-to-your-data
```
and then start ParaView *from the shell*, e.g., on macOS:
```
/Applications/ParaView-5.11.2.app/Contents/MacOS/paraview
```
From the File menu, select "Load State" to load one of .pvsm (ParaView state) files provided in this repo. Assuming you have the appropriate data file(s), it should run the pipeline and display results.