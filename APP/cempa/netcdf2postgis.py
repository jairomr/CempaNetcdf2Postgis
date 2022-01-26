from datetime import datetime

import numpy as np
import pandas as pd
from netCDF4 import Dataset

from cempa.config import is_goias, lats, logger, lons, ormdtype, settings
from cempa.functions import exists_in_the_bank, get_list_nc, save_hash
from cempa.hash import data_frame2hash, generate_file_md5
from cempa.model import engine


def get_time(name: str) -> str:
    date_time_str = (
        name.split("/")[-1].replace("Go05km-A-", "").replace("00-g1.nc", "")
    )
    return str(datetime.strptime(date_time_str, "%Y-%m-%d-%H%M%S"))


def netcsf2sql(file_name: str, rootgrp: Dataset) -> bool:
    error = False
    for name in settings.vars:
        try:
            tempc = rootgrp.variables[name][:]
            logger.info(
                f"Processando varivael {name} de {file_name.split('/')[-1]}"
            )

            vtime, latitudes_grid, longitudes_grid = [
                x.flatten()
                for x in np.meshgrid(
                    get_time(file_name), lats, lons, indexing="ij"
                )
            ]
            if len(np.squeeze(tempc)) == 19:
                camadas = {
                    f"{name}_{c:02}": var.flatten()
                    for c, var in enumerate(np.squeeze(tempc), 1)
                }
            else:
                camadas = {f"{name}": np.squeeze(tempc).flatten()}
            temp_df = pd.DataFrame(
                {
                    "datetime": vtime,
                    "goias": is_goias["goias"].array,
                    **camadas,
                    "point_gid": is_goias.index,
                }
            )
            temp_df = temp_df.dropna(subset=["goias"])
            temp_df["datetime"] = pd.to_datetime(temp_df["datetime"])
            temp_df = temp_df.drop(["goias"], axis=1).set_index("datetime")

            df_hash = data_frame2hash(name, temp_df)

            if not exists_in_the_bank(df_hash):
                logger.info(
                    f"salvando no banco {file_name.split('/')[0]} {name}"
                )

                try:
                    temp_df.to_sql(
                        name, engine, dtype=ormdtype[name], if_exists="append"
                    )
                    save_hash(df_hash)

                except Exception:
                    error = True
                    logger.exception("What?!")
            else:
                logger.info("Ja tem no banco")
        except Exception:
            logger.exception("What?!")
            error = True
    return error


def main() -> None:
    for file in get_list_nc(settings.FILES_NC):
        logger.info(file)
        file_hash = generate_file_md5(file)
        if not exists_in_the_bank(file_hash):
            rootgrp = Dataset(file)
            if not netcsf2sql(file, rootgrp):
                save_hash(file_hash)
            else:
                logger.warning("Teve error")
        else:
            logger.info("File ja foi salvo no banco")


if __name__ == "__main__":
    main()
