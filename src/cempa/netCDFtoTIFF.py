from os.path import isfile
from time import time

import numpy as np

from cempa.config import logger, settings
from cempa.functions import create_folder_for_tiffs, get_time
from generatmap.map import creat_map_file


def nc2tiff(xr_file, name, coll_name, file_name, id_level=None):
    """_summary_

    Args:
        name (_type_): _description_
        coll_name (_type_): _description_
        file_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    file_date = get_time(file_name,True)
    path_level1 = f'{settings.DIRMAP}/{file_date}'
    create_folder_for_tiffs(path_level1, name)
    name_tif = f'{path_level1}/{name}/{coll_name}.tif'
    name_map = f'{path_level1}/{name}/{coll_name}.map'
    if (
        isfile(name_tif)
        and isfile(f'{name_map}')
        and not settings.forceCreateFiles
    ):
        logger.info('Tiff e map ja foi gerado')
        return None
    start_time = time()
    logger.info(
        f'Criando tiff /{file_date}/{name}/{coll_name}.tif'
    )

    raster = xr_file[name]
    if isinstance(id_level, int):
        raster = raster.isel(lev_2=id_level).rio.set_spatial_dims('lon', 'lat')
    else:
        raster = raster.rio.set_spatial_dims('lon', 'lat')
    min_max = (
        round(np.nanmin(raster), 2),
        round(np.nanmax(raster) + 0.05, 2),
    )
    raster.rio.set_crs('epsg:4674')
    raster.rio.to_raster(name_tif)
    creat_map_file(name_tif, coll_name, min_max=min_max, file_date=file_date, geotiff=True)
    logger.info(f'Tempo de crianção para tif e map: {time() - start_time}s')
    return None
