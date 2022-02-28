from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from cempa.config import settings

Base = declarative_base()
keepalive_kwargs = {
    "keepalives": 1,
    "keepalives_idle": 30,
    "keepalives_interval": 5,
    "keepalives_count": 5,
}

engine = create_engine(settings.dblink, pool_pre_ping=True, **keepalive_kwargs)

def create_session():
    Session = sessionmaker(bind=engine)
    return Session()
