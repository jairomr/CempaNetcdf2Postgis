from jinja2 import Environment, PackageLoader, select_autoescape
from sqlalchemy import select

from cempa.functions import get_min_max, get_pallet
from cempa.db import session
from cempa.model import StyleMap
from cempa.config import settings, logger

def creat_map_file(file_name,  coll_name, min_max= False, geotiff = False):
    logger.info("Criando o .map para o tiff")
    env = Environment(
        loader=PackageLoader("generatmap"), autoescape=select_autoescape()
    )

    with open(file_name.replace(".tif",".map"), "w") as file_object:
        template = env.get_template("cempa.map")
        row = {}
        try:
            row = session.execute(select(
                StyleMap).where(StyleMap.coll_table == coll_name)
            ).first()[0].to_dict()
            logger.info(
                f"Creating table layer '{row['table_name']}' from variable '{row['coll_table']}'"
            )
            _minmax = get_min_max(row.coll_table, row.table_name)
        except:
            logger.info("Gerando .map com dados padrao")
            row["view_name"] = f"{coll_name}_geotiff"
            row["ows_title"] = coll_name
            row["ows_abstract"] = coll_name
            row["palette"] = "magma"
        row["geotiff"] = geotiff
        if geotiff:
            row["coll_view"] = "pixel"
            row["file_name"] = file_name
        if not min_max == False:
            _minmax = min_max
        try:
            file_object.write(
                template.render(
                {
                    **row,
                    "styles": get_pallet(
                    *_minmax,
                    row["palette"],
                ),
                }
            ))
        except:
            logger.exception("Error")
            
            
def creat_by_bd():
    env = Environment(
        loader=PackageLoader("generatmap"), autoescape=select_autoescape()
    )

    with open(settings.MAPFILE, "w") as file_object:
        template = env.get_template("cempa.map")
        for row in session.execute(select(StyleMap)).all():
            try:
                row = row[0]
                logger.info(
                    f"Creating table layer '{row.table_name}' from variable '{row.coll_table}'"
                )
                file_object.write(
                    template.render(
                        {
                            **row.to_dict(),
                            "styles": get_pallet(
                                *get_min_max(row.coll_table, row.table_name),
                                row.palette,
                            ),
                        }
                    )
                )
            except:
                logger.exception("Error")