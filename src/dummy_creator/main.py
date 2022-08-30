import json
import os

from typing import Dict, List, Optional, Union

from .core import create_data


def create_dummy(params: List[Dict[str, str]],
                 input_files: Optional[List[str]] = None,
                 out_file: bool = False) -> Dict[str, Union[int, float]]:
    data: dict = {}

    if input_files is None:
        assert issubclass(type(params), list)
        for i, param in enumerate(params):
            data[i] = create_data(param)
    else:
        assert issubclass(type(input_files), list)
        for i, input_file in enumerate(input_files):
            assert os.path.isfile(input_file)
            with open(input_file, 'r') as f:
                parameters = json.load(f)
            data[i] = create_data(parameters, out_file=out_file)

    return data
