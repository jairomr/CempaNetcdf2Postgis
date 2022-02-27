from jinja2 import Environment, PackageLoader, select_autoescape
from sqlalchemy import select

from cempa.config import logger, settings
from cempa.db import create_session
from cempa.functions import get_min_max, get_pallet
from cempa.model import StyleMap


def creat_map_file(file_name, coll_name, min_max=False, geotiff=False):
    logger.info('Criando o .map para o tiff')
    env = Environment(
        loader=PackageLoader('generatmap'), autoescape=select_autoescape()
    )

    with open(file_name.replace('.tif', '.map'), 'w') as file_object:
        template = env.get_template('cempa.map')
        row = {}
        try:
            session = create_session()
            row = (
                session.execute(
                    select(StyleMap).where(StyleMap.coll_table == coll_name)
                )
                .first()[0]
                .to_dict()
            )
            logger.info(
                "Creating layer '{}' from variable '{}'".format(
                    row['table_name'], row['coll_table']
                )
            )
            _minmax = get_min_max(row.coll_table, row.table_name)
        except:
            logger.info('Gerando .map com dados padrao')
            row['view_name'] = f'{coll_name}_geotiff'
            row['ows_title'] = coll_name
            row['ows_abstract'] = coll_name
            row['palette'] = 'magma'
        row['geotiff'] = geotiff
        if geotiff:
            row['coll_view'] = 'pixel'
            row['file_name'] = file_name
        if not (min_max is False):
            _minmax = min_max
        try:
            file_object.write(
                template.render(
                    {
                        'host': settings.dbmap_host,
                        'port': settings.dbmap_port,
                        'dbname': settings.dbmap_dbname,
                        'user': settings.dbmap_user,
                        'password': settings.dbmap_password,
                        **row,
                        'styles': get_pallet(
                            *_minmax,
                            row['palette'],
                        ),
                    }
                )
            )
        except:
            logger.exception('Error')


def creat_by_bd():
    env = Environment(
        loader=PackageLoader('generatmap'), autoescape=select_autoescape()
    )

    with open(settings.MAPFILE, 'w') as file_object:
        template = env.get_template('cempa.map')
        session = create_session()
        for row in session.execute(select(StyleMap)).all():
            try:
                row = row[0]
                logger.info(
                    "Creating layer '{}' from variable '{}'".format(
                        row['table_name'], row['coll_table']
                    )
                )
                file_object.write(
                    template.render(
                        {
                            **row.to_dict(),
                            'styles': get_pallet(
                                *get_min_max(row.coll_table, row.table_name),
                                row.palette,
                            ),
                        }
                    )
                )
            except:
                logger.exception('Error')
