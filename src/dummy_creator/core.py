import csv
import os

from .aux import _create_dummy


def create_data(parameters: dict) -> dict:
    keys = parameters.keys()

    os.makedirs('csv', exist_ok=True)
    for key in keys:
        data: dict = _create_dummy(parameters[key])
        output_file = 'csv/' + key + '.csv'
        with open(output_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(data['header'])
            writer.writerows(data['rows'])

    return data
