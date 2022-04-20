import json
import os

from typing import Dict, List, Tuple

from .core import create_data


def create_dummy(input_file: str = None, **kwargs):
    is_file = os.path.isfile(input_file)
    if input_file and is_file:
        with open(input_file, 'r') as f:
            parameters = json.load(f)
    else:
        try:
            parameters = dict(kwargs['parameters'])
        except KeyError:
            print('Please specify parameter of json file representting parameter.')
            return

    keys = list(create_data(parameters))

    return keys
