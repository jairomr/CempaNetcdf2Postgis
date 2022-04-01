from os import environ, mkdir
from os.path import isdir
from shutil import rmtree

import click
from dynaconf import Dynaconf

from cirrus.model import clear_tables
#from cirrus.netcdf2postgis import main
from cirrus.util.config import logger
from cirrus.dowloads import downloads_files

initial_config = Dynaconf(
    envvar_prefix='CEMPA',
    settings_files=['settings.toml', '.secrets.toml'],
)


@click.command()
@click.option('--force_save_bd/--no-force_save_bd', default=False)
def cli_main(force_save_bd):
    environ['CEMPA_FORCE_SAVE_BD'] = str(force_save_bd).lower()

    logger.info(
        f'Numero de pool {initial_config.N_POOL} force_save = {initial_config.FORCE_SAVE_BD}'
    )
    if downloads_files():
        clear_tables()
        
        pass
    
    #main(initial_config.FORCE_SAVE_BD)


if __name__ == '__main__':
    cli_main()
