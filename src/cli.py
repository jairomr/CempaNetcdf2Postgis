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
    if clear:
        clear_tables()
        path = initial_config.DIRMAP
        if isdir(path):
            rmtree(path)
        if not isdir(path):
            mkdir(path)
    if not path == '':
        environ['CEMPA_FILES_NC'] = f'{path}'
    environ['CEMPA_FORCE_SAVE_BD'] = str(force_save_bd).lower()
    logger.info(f'Numero de pool {initial_config.N_POOL}')
    main()


if __name__ == '__main__':
    cli_main()
