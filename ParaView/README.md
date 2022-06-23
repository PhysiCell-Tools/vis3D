## ParaView to visualize PhysiCell 3D data

ParaView is an open-source, multi-platform data analysis and visualization application. Users create a pipeline to read data, apply filters, and render results. For PhysiCell data, we provide sample pipelines that contain a custom data reader and relevant filters (in an editable Python script).

This README serves as an updated version of an earlier [blog post](http://www.mathcancer.org/blog/paraview-for-physicell-part-1/), but much of the information there is still relevant.

Dependencies:

* We recommend using the [Anaconda Python distribution](https://www.anaconda.com/products/distribution). The current (June 2022) version provides Python 3.9.x (If you are using a Mac Silicon/arm64 computer, we recommend downloading the x86_64 version, not the arm64 version. The latter does not seem to provide all the necessary Python modules).

* Download [ParaView](https://www.anaconda.com/products/distribution). The current (June 2022) version is 5.10.1 and uses Python 3.9.x. NOTE: it is *required* that your Python version (above) matches that being used by ParaView, e.g., 3.9.

Usage:

You need to set an environment variable that will tell ParaView the location of your (Anaconda) Python installation, e.g., in a bash shell:
```
export PV_VENV=/Users/heiland/opt/anaconda3
```
Optionally, as discussed in the blog post, you can specify where your 3D PhysiCell data is located via:
```
export PHYSICELL_DATA=full-path-to-your-data
```
and then start ParaView *from the shell*, e.g., on macOS:
```
/Applications/ParaView-5.10.1.app/Contents/MacOS/paraview
```
From the File menu, select "Load State" to load one of .pvsm (ParaView state) files provided in this repo. Assuming you have the appropriate data file(s), it should run the pipeline and display results.