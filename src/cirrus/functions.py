import os
from datetime import datetime
from glob import glob
from os.path import isdir

import seaborn as sns

from cirrus.model import FileHash
from cirrus.db import create_session

from cirrus.config import logger


def get_time(name: str, return_txt=False) -> str:
    date_time_str = (
        name.split('/')[-1].replace('Go05km-A-', '').replace('00-g1.nc', '')
    )
    if return_txt:
        return date_time_str.replace('-', '')
    return str(datetime.strptime(date_time_str, '%Y-%m-%d-%H%M%S'))


def get_list_nc(path_files: str):
    return glob(f'{path_files}/*.nc')


def get_min_max(coll_table, table_name):
    try:
        _min, _max = session.execute(
            f'select min({coll_table}), max({coll_table}) from {table_name}'
        ).all()[0]
        return (round(_min, 2), round(_max + 0.05, 2))
    except:
        return (0, 1)


def exists_in_the_bank(file_hash: str):
    session = create_session()
    try:
        is_valid  = session.query(FileHash).filter_by(file_hash = file_hash).first()
        if is_valid.file_hash == file_hash:
            return True
        return False
    except AttributeError:
        return False
    except:
        logger.exception('Error exists_in_the_bank')
        return True


def save_hash(str_hash: str) -> None:
    session = create_session()
    session.add(FileHash(file_hash=str_hash))
    session.commit()


def get_pallet(_min, _max, color_name='magma', n_class=25):
    yield from [
        {
            'min': ((_max - _min) / n_class) * n + _min,
            'max': ((_max - _min) / n_class) * (n + 1) + _min,
            'color': color,
        }
        for n, color in enumerate(
            sns.color_palette(color_name, n_colors=n_class).as_hex()
        )
    ]


def create_folder_for_tiffs(path_level1, name):
    if not isdir(path_level1):
        os.mkdir(path_level1)
    if not isdir(f'{path_level1}/{name}'):
        os.mkdir(f'{path_level1}/{name}')
