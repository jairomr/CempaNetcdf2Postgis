from os import environ

import click

from cempa.netcdf2postgis import main


@click.command()
@click.option("--path", default="", help="Caminho para os aqrivos netcdf.")
def cli_main(path):
    if not path == "":
        environ["CEMPA_FILES_NC"] = f"{path}"
    main()


if __name__ == "__main__":
    cli_main()
