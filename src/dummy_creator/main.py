import json
import os

from typing import List, Optional

from .core import create_data


def create_dummy(input_files: Optional[List[str]] = None, **kwargs):
    if input_files is None:
        try:
            parameters = dict(kwargs['parameters'])
        except KeyError:
            print('Please specify parameter of json file representting parameter.')
            return
        return create_data(parameters)

    assert issubclass(type(input_files), list), 'assertion!!!'

    data: dict = {}
    for i, input_file in enumerate(input_files):
        assert os.path.isfile(input_file)
        with open(input_file, 'r') as f:
            parameters = json.load(f)
        data[i] = create_data(parameters)

    return data
