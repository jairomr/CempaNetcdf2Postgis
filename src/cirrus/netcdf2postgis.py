import shutil
from glob import glob
from multiprocessing import Pool
from time import time

import numpy as np
import pandas as pd
import xarray as xr
from netCDF4 import Dataset

from cirrus.netCDFtoTIFF import nc2tiff
from cirrus.util.config import is_goias, lats, logger, lons, ormdtype, settings
from cirrus.util.db import engine, save_df_bd
from cirrus.util.hash import data_frame2hash, generate_file_md5

from cirrus.util.functions import (  # isort:skip
    exists_in_the_bank,
    get_list_nc,
    get_time,
    save_hash,
)


def netcsf2sql(file_name: str, rootgrp: Dataset, xr_file, force_save_db):
    """_summary_

    Args:
        file_name (str): _description_
        rootgrp (Dataset): _description_

    Returns:
        bool: _description_
    """
    error = False
    for name in settings.vars:
        try:
            tempc = rootgrp.variables[name][:]
            logger.info(
                f"Processando varivael {name} de {file_name.split('/')[-1]}"
            )

            vtime, *_ = [
                x.flatten()
                for x in np.meshgrid(
                    get_time(file_name), lats, lons, indexing='ij'
                )
            ]
            camadas = {}
            if len(np.squeeze(tempc)) == 19:
                for c, var in enumerate(np.squeeze(tempc), 1):
                    camadas[f'{name}_{c:02}'] = var.flatten()
                    nc2tiff(xr_file, name, f'{name}_{c:02}', file_name, c - 1)
            else:
                camadas = {f'{name}': np.squeeze(tempc).flatten()}
                nc2tiff(xr_file, name, name, file_name)
            temp_df = pd.DataFrame(
                {
                    'datetime': vtime,
                    'goias': is_goias['goias'].array,
                    **camadas,
                    'point_gid': is_goias.index,
                }
            )
            temp_df = temp_df.dropna(subset=['goias'])
            temp_df['datetime'] = pd.to_datetime(temp_df['datetime'])
            temp_df = temp_df.drop(['goias'], axis=1)  # .set_index('datetime')

            df_hash = data_frame2hash(name, temp_df)

            if force_save_db or not exists_in_the_bank(df_hash):
                logger.info(
                    f"salvando no banco {file_name.split('/')[0]} {name}"
                )

                try:
                    # temp_df.to_sql(
                    #    name, engine, dtype=ormdtype[name], if_exists='append'
                    # )
                    save_df_bd(temp_df, name)
                    save_hash(df_hash)

                except Exception:
                    error = True
                    logger.exception('Erro ao salva no Banco?!')
            else:
                logger.info('Ja tem no banco')
        except Exception:
            logger.exception('What?!')
            error = True
    return error


def load_file(args):
    """_summary_

    Args:
        file (_type_): _description_

    Returns:
        _type_: _description_
    """
    file, force_save_db = args
    logger.info(f'force = {force_save_db} in {file}')
    file_hash = generate_file_md5(file)
    if (not exists_in_the_bank(file_hash)) or settings.IGNOREHASHFILE:
        rootgrp = Dataset(file)
        xr_file = xr.open_dataset(file)
        if not netcsf2sql(file, rootgrp, xr_file, force_save_db):
            save_hash(file_hash)
            return {'file': file, 'status': 'sucesso'}
        else:
            logger.warning('Teve error')
            return {'file': file, 'status': 'error'}
    else:
        logger.info('File ja foi salvo no banco')
        return {
            'file': file,
            'status': 'sucesso',
            'mensagem': 'Ja foi salvo no banco',
        }


def main(force_save_db=False):
    """_summary_"""
    main_start = time()

    with Pool(settings.N_POOL) as workers:
        result = workers.map(
            load_file,
            [(file, force_save_db) for file in get_list_nc(settings.BINFILES)],
        )
    # logger.info(result)
    logger.info(
        f'Numero de pool {settings.N_POOL} force_save = {force_save_db}'
    )
    logger.info(f'tempo total = {time() - main_start}s')
    logger.info(f'criando {settings.BIGTIFF}')
    with open(settings.BIGTIFF, 'wb') as wfd:
        for file in glob(f'{settings.DIRMAP}/*/*/*.map'):
            with open(file, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)


if __name__ == '__main__':
    main()
