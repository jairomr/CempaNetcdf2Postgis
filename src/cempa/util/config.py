from pickle import load

from dynaconf import Dynaconf
from loguru import logger
from pandas import read_csv

logger.add(
    '../sys.log',
    format='[{time} | {process.id} | {level: <8}] {module}.{function}:{line} {message}',
    rotation='500 MB',
)

logger.add(
    '../syserror.log',
    format='[{time} | {process.id} | {level: <8}] {module}.{function}:{line} {message}',
    rotation='500 MB',
    level='WARNING',
)


settings = Dynaconf(
    envvar_prefix='CEMPA',
    settings_files=['settings.toml', '.secrets.toml'],
)


is_goias = read_csv('./metadata/points_go.csv', index_col='gid')
with open('./metadata/lonlat.obj', 'rb') as tfile:
    lons, lats = load(tfile)

with open('./metadata/ormdtype.obj', 'rb') as tfile:
    ormdtype = load(tfile)
