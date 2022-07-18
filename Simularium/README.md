Workflow to convert a PhysiCell model's results (`/output`) to a Simularium object that can be uploaded and viewed at https://simularium.allencell.org/viewer

You will need to `pip install simulariumio` (we assume you've already installed the Anaconda Python 3.x distribution).

See`https://github.com/simularium/simulariumio/blob/main/examples/Tutorial_physicell.ipynb` for the basic Jupyter notebook procedure for 
converting your PhysiCell data and uploading to the Simularium viewer. But in the `path_to_output_dir` line (see below), you may need
to provide the *full* path and not a relative path:

```
example_data = PhysicellData(
    timestep=30.0,
    path_to_output_dir="/Users/heiland/PhysiCell/output",
...
```
