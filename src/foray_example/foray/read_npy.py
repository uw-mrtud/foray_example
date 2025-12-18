import numpy as np
from foray import ForayConfig, Port, FilePicker


def config():
    return (
        ForayConfig()
        .outputs(
            {
                "array": Port.array(Port.complex, [None, None]),
            }
        )
        .parameters({"file_path": FilePicker()})
    )


def compute(input, params):
    file_name = params["file_path"]
    array = np.load(file_name)
    return {"array": array}
