from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData
from sqlalchemy import Table

from cempa.config import settings, logger

Base = declarative_base()

engine = create_engine(settings.dblink, pool_pre_ping=True)

def create_session():
    Session = sessionmaker(bind=engine)
    return Session()




def save_df_bd(df,name):
    try:
        conn = engine.connect() 
        listToWrite = df.to_dict(orient='records')

        metadata = MetaData(bind=engine)
        table = Table(name, metadata, autoload=True)

        # Open the session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Inser the dataframe into the database in one bulk
        conn.execute(table.insert(), listToWrite)

        # Commit the changes
        session.commit()

        # Close the session
        session.close()
    except Exception:
        logger.exception('Erro ao salvar no banco?!')