from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from cempa.config import settings

Base = declarative_base()
engine = create_engine(settings.dblink)

def create_session():
    Session = sessionmaker(bind=engine)
    return Session()
