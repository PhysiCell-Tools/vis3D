from IPython.display import Image
import numpy as np
from simulariumio.physicell import PhysicellConverter, PhysicellData
from simulariumio import UnitData, MetaData, DisplayData, DISPLAY_TYPE, ModelMetaData

box_size = 800.0  # [-400,400]

my_model_data = PhysicellData(
    timestep=1.0,
    path_to_output_dir="/Users/heiland/dev/PhysiCell_v1.10.4/output",
    meta_data=MetaData(
        box_size=np.array([box_size, box_size, 100.0]),
        scale_factor=0.01,
        trajectory_title="Some parameter set",
        model_meta_data=ModelMetaData(
            title="The PhysiCell 'interaction' sample model",
            version="8.1",
            authors="Paul Macklin, et al",
            description=(
                "An agent-based model to demonstrate relatively simple immunology."
            ),
            doi="10.1016/j.bpj.2016.02.002",
            source_code_url="https://github.com/allen-cell-animated/simulariumio",
            source_code_license_url="https://github.com/allen-cell-animated/simulariumio/blob/main/LICENSE",
            input_data_url="https://allencell.org/path/to/native/engine/input/files",
            raw_output_data_url="https://allencell.org/path/to/native/engine/output/files",
        ),
    ),
    nth_timestep_to_read=1,
    display_data={
        0: DisplayData(
            name="bacteria",
            display_type=DISPLAY_TYPE.OBJ,
            url="bacteria.obj",
            color="#dfdacd",
        ),
        1: DisplayData(
            name="bacteria",
            color="#0080ff",
        ),
    },
    phase_names={
        0: {4: "G0G1"},
        1: {4: "G0G1"},
    },
    time_units=UnitData("s"),  # seconds
)

print("calling PhysicellConverter...\n")
PhysicellConverter(my_model_data).write_JSON("interaction")

print("\nNow click 'Load model' from https://simularium.allencell.org/viewer and upload this file.")
