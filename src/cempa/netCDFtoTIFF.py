import os
from os.path import isdir, isfile
from time import time

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from matplotlib.tri import LinearTriInterpolator, Triangulation
from rasterio.crs import CRS
from rasterio.transform import Affine

from cempa.config import lats, logger, lons, settings
from cempa.functions import get_time
from generatmap.map import creat_map_file


def nc2tiff(name, var, coll_name, file_name):
    path_level1 = f"{settings.DIRMAP}/{get_time(file_name,True)}"
    if not isdir(path_level1):
        os.mkdir(path_level1)
    if not isdir(f"{path_level1}/{name}"):
        os.mkdir(f"{path_level1}/{name}")
    name_tif = f"{path_level1}/{name}/{coll_name}.tif"
    name_map = f"{path_level1}/{name}/{coll_name}.map"
    if (
        isfile(name_tif)
        and isfile(f"{name_map}")
        and not settings.forceCreateFiles
    ):
        logger.info("Tiff e map ja foi gerado")
        return None
    start_time = time()
    logger.info(
        f"Criando tiff /{get_time(file_name,True)}/{name}/{coll_name}.tif"
    )
    vtime, latitudes_grid, longitudes_grid = [
        x.flatten()
        for x in np.meshgrid(get_time(file_name), lats, lons, indexing="ij")
    ]
    tmp_var = var
    data = {
        "date_time": vtime,
        "lat": latitudes_grid,
        "lon": longitudes_grid,
        f"{name}": tmp_var,
    }
    temp_df = pd.DataFrame(data)
    min_max = (
        round(np.nanmin(tmp_var), 2),
        round(np.nanmax(tmp_var) + 0.05, 2),
    )
    tgpdf = gpd.GeoDataFrame(
        temp_df, geometry=gpd.points_from_xy(temp_df.lon, temp_df.lat)
    )
    points3d = tgpdf.set_crs(epsg=4674)

    totalPointsArray = np.zeros([points3d.shape[0], 3])
    # iteration over the geopandas dataframe
    for index, point in points3d.iterrows():
        pointArray = np.array(
            [
                point.geometry.coords.xy[0][0],
                point.geometry.coords.xy[1][0],
                point[name],
            ]
        )
        totalPointsArray[index] = pointArray

    # triangulation function
    triFn = Triangulation(totalPointsArray[:, 0], totalPointsArray[:, 1])
    # linear triangule interpolator funtion
    linTriFn = LinearTriInterpolator(triFn, totalPointsArray[:, 2])

    # define raster resolution in (m)
    rasterRes = settings.rasterRes  # 0.01

    xCoords = np.arange(
        totalPointsArray[:, 0].min(),
        totalPointsArray[:, 0].max() + rasterRes,
        rasterRes,
    )
    yCoords = np.arange(
        totalPointsArray[:, 1].min(),
        totalPointsArray[:, 1].max() + rasterRes,
        rasterRes,
    )
    zCoords = np.zeros([yCoords.shape[0], xCoords.shape[0]])

    # loop among each cell in the raster extension
    for indexX, x in np.ndenumerate(xCoords):
        for indexY, y in np.ndenumerate(yCoords):
            tempZ = linTriFn(x, y)
            # filtering masked values
            if tempZ == tempZ:
                zCoords[indexY, indexX] = tempZ
            else:
                zCoords[indexY, indexX] = np.nan

    transform = Affine.translation(
        xCoords[0] - rasterRes / 2, yCoords[0] - rasterRes / 2
    ) * Affine.scale(rasterRes, rasterRes)

    triInterpRaster = rasterio.open(
        name_tif,
        "w",
        driver="GTiff",
        height=zCoords.shape[0],
        width=zCoords.shape[1],
        count=1,
        dtype=zCoords.dtype,
        # crs='+proj=latlong',
        crs={"init": "epsg:4674"},
        transform=transform,
    )
    triInterpRaster.write(zCoords, 1)
    triInterpRaster.close()
    creat_map_file(name_tif, coll_name, min_max=min_max, geotiff=True)
    logger.info(f"Tempo de crianção para tif e map: {time() - start_time}")
    return None
