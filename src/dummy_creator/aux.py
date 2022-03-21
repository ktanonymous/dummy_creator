import math
import numpy as np
import random
import sys

from .const import LOG_NORMAL, NORMAL, RANDOM, UNIFORM


def _create_dummy(parameters: dict) -> dict:
    data = {}

    try:
        n_data: int = parameters['number']
    except KeyError:
        print('Please define number of data to create.')
        sys.exit()

    try:
        labels: dict = parameters['label']
    except KeyError:
        labels = None

    try:
        dist: str = parameters['dist']
    except KeyError:
        print('distribution is "uniform" because was undeclared.')
        dist = UNIFORM

    # 連続値の場合は不適切なネーミング
    data['header'] = [
        'label',
        'label_name',
    ]
    data['rows'] = gen_data(parameters, n_data, labels=labels, dist=dist)

    return data


def gen_data(parameters, n_data: int, labels: dict, dist: str) -> list:
    # 連続値と離散値の区別をどうするか
    # 連続値なら最大最小、離散値なら各値が必要
    distribution = {
        # 対数正規分布
        LOG_NORMAL: lognormal,
        # 正規分布
        NORMAL: normal,
        # ランダムピックアップ
        RANDOM: random_gen,
        # 一様分布
        UNIFORM: uniform,
    }

    rows = distribution[dist](parameters, labels, n_data)
    return rows


def lognormal(parameters, labels: dict, n_data: int):
    try:
        median = parameters['median']
        mode = parameters['mode']
    except KeyError:
        print('median of disitribution is 1.0 because was undeclared.')
        median = 1.0
        mode = median

    mu = math.log(median)
    sigma = math.sqrt(mu - math.log(mode))

    rows = np.random.lognormal(mu, sigma, size=(n_data, 1))
    return rows


def normal(parameters, labels: dict, n_data: int):
    try:
        loc = parameters['mean']
        scale = parameters['std']
    except KeyError:
        print('mean(std) of disitribution is 0.0(1.0) because was undeclared.')
        loc = 0.0
        scale = 1.0

    np.random.normal(loc=loc, scale=scale, size=(n_data, 1))
    pass


def uniform(parameters, labels: dict, n_data: int):
    try:
        low = parameters['min']
        high = parameters['max']
    except KeyError:
        print('minimum(maximum) of disitribution is 0.0(1.0) because was undeclared.')
        low = 0.0
        high = 1.0

    # low 以上 high 未満の一様分布
    np.random.uniform(low=low, high=high, size=(n_data, 1))
    return rows


def random_gen(parameters, labels: dict, n_data: int):
    population = list(labels.items())

    try:
        weights = list(parameters['weights'].values())
    except KeyError:
        weights = None

    rows = random.choices(population=population, weights=weights, k=n_data)
    return rows
