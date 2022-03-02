"""生成データ数、データ種、データ分布を指定してデータを生成させる？
json例？
{
    name1: {
        number: 1000,
        kinds: {
            name1,
            name2,
            ...
        }
        dist: random/etc.
    },
    name2: {
        ...
    },
    ...
}
"""
import json
import os

from typing import Dict, List, Tuple


def create_dummy(n_data: int = 1000, *args, **kwargs):
    try:
        input_file = kwargs['input_file']
    except KeyError:
        input_file = None

    is_file = os.path.isfile(input_file)
    if input_file and is_file:
        with open(input_file, 'r') as f:
            parameters = json.laod(f)
    else:
        pass
