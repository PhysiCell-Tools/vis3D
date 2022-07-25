Workflow to convert a PhysiCell model's results (`/output`) to a Simularium file that can be uploaded and viewed at https://simularium.allencell.org/viewer

You will need to `pip install simulariumio[physicell]` (we assume you've already installed the Anaconda Python 3.x distribution).

Finally, from the directory of your model's output files:
```
python convert_to_simularium.py    # you want to customize this script for your data
```

This will generate a Simularium file which you can upload from https://simularium.allencell.org/viewer
