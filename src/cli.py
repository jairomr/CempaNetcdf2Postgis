from os import environ, mkdir
from os.path import isdir
from shutil import rmtree

import click
from dynaconf import Dynaconf

from cempa.model import clear_tables
from cempa.netcdf2postgis import main
from cempa.config import logger

initial_config = Dynaconf(
    envvar_prefix='CEMPA',
    settings_files=['settings.toml', '.secrets.toml'],
)


@click.command()
@click.option('--path', default='', help='Caminho para os aqrivos netcdf.')
@click.option('--clear/--no-clear', default=False)
@click.option('--force_save_bd/--no-force_save_bd', default=False)
def cli_main(path, clear, force_save_bd):
    
    if not path == '':
        environ['CEMPA_FILES_NC'] = f'{path}'
    environ['CEMPA_FORCE_SAVE_BD'] = str(force_save_bd).lower()
    
    if clear:
        clear_tables()
        my_dir = initial_config.DIRMAP
        if isdir(my_dir):
            rmtree(my_dir)
        if not isdir(my_dir):
            mkdir(my_dir)
    logger.info(f'Numero de pool {initial_config.N_POOL} force_save = {initial_config.FORCE_SAVE_BD}')
    main()


if __name__ == '__main__':
    cli_main()
