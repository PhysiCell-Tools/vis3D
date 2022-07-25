import numpy as np
from simulariumio.physicell import PhysicellConverter, PhysicellData
from simulariumio import UnitData, MetaData, DisplayData, DISPLAY_TYPE, ModelMetaData

my_model_data = PhysicellData(
    timestep=1.0,
    path_to_output_dir="data/interaction_model/", # point to Physicell/output/
    meta_data=MetaData(
        box_size=np.array([800.0, 800.0, 100.0]),
        scale_factor=0.01,
        trajectory_title="Some parameter set",
        model_meta_data=ModelMetaData(
            title="Some agent-based model",
            version="8.1",
            authors="A Modeler",
            description=(
                "A PhysiCell model run with some parameter set"
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
            name="tumor cell",
            display_type=DISPLAY_TYPE.OBJ,
            url="tumor_cell.obj",
            color="#dfdacd",
        ),
        1: DisplayData(
            name="motile tumor cell",
            color="#0080ff",
        ),
    },
    phase_names={
        0: {
            14: "G0G1",
            100: "Apoptotic"
        },
        1: {14: "G0G1"},
    },
    time_units=UnitData("s"),  # seconds
)

print("calling PhysicellConverter...\n")
PhysicellConverter(my_model_data).save("interaction_model")
