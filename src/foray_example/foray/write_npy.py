import numpy as np
from foray import ForayConfig, Port, FilePicker


def config():
    return (
        ForayConfig()
        .inputs(
            {
                "array": Port.array(Port.complex, [None, None]),
            }
        )
        .parameters({"file_path": FilePicker()})
    )


def compute(input, params):
    array = input["array"]
    file_name = params["file_path"]
    np.save(file_name, array)
    return {}
