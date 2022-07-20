Workflow to convert a PhysiCell model's results (`/output`) to a Simularium object that can be uploaded and viewed at https://simularium.allencell.org/viewer

You will need to `pip install simulariumio` (we assume you've already installed the Anaconda Python 3.x distribution).

And until the simulariumio pkg is updated for the newer pyMCDS, you need to overwrite what is there withe "_v3" version, e.g. (replacing 'heiland' with your username):
```
cp pyMCDS_v3.py /Users/heiland/anaconda3/lib/python3.9/site-packages/simulariumio/physicell/dep/pyMCDS.py
```

Finally, from the directory of your model's output files:
```
python convert_to_simularium.py    # you want to customize this script for your data
```

This will generate a Simularium file which you can upload from https://simularium.allencell.org/viewer
