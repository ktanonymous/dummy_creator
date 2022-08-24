import csv
import os

from .aux import _create_dummy
from typing import Iterable


def create_data(parameters: dict, out_file: bool = False) -> dict:
    keys = parameters.keys()

    if out_file:
        os.makedirs('csv', exist_ok=True)
    data = _create_data(keys, parameters, out_file)

    return data


def _create_data(keys: Iterable, parameters: dict, out_file: bool) -> dict:
    data: dict = {}
    for key in keys:
        _data = _create_dummy(parameters[key])

        if out_file:
            output_file = 'csv/' + key + '.csv'
            with open(output_file, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(_data['header'])
                writer.writerows(_data['rows'])

        data[key] = _data

    return data
