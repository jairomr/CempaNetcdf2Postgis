from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import Column, ForeignKey, delete
from sqlalchemy.types import DateTime, Float, Integer, String

from cirrus.util.db import Base, create_session, engine


class StyleMap(Base):
    __tablename__ = 'stylemap'
    id = Column(Integer, primary_key=True)
    table_name = Column(String)
    coll_table = Column(String)
    view_name = Column(String)
    coll_view = Column(String)
    ows_title = Column(String)
    ows_abstract = Column(String)
    metrica = Column(String)
    palette = Column(String)
    max_mix_query = Column(String)

    def to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result


class FileHash(Base):
    __tablename__ = 'files_hashs'
    id = Column(Integer, primary_key=True)
    file_hash = Column(String)
    datetime = Column(DateTime, default=datetime.now, index=True)


class Points(Base):
    __tablename__ = 'points'
    gid = Column(Integer, primary_key=True)
    geom = Column(Geometry('POINT', 4674), index=True)
    lat = Column(Float)
    lon = Column(Float)
    uf = Column(String(4), index=True)
    bioma = Column(String(100), index=True)
    cd_geocmu = Column(String(100), index=True)
    amaz_legal = Column(Integer, index=True)
    matopiba = Column(Integer, index=True)
    municipio = Column(String(200), index=True)


class CempaSMOIST1(Base):
    __tablename__ = 'smoist1'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaSMOIST2(Base):
    __tablename__ = 'smoist2'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaSMOIST3(Base):
    __tablename__ = 'smoist3'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaSMOIST4(Base):
    __tablename__ = 'smoist4'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaALBEDT(Base):
    __tablename__ = 'albedt'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaTEMPC(Base):
    __tablename__ = 'tempc'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_100  = Column(Float) 
    lev_150  = Column(Float) 
    lev_200  = Column(Float) 
    lev_250  = Column(Float) 
    lev_300  = Column(Float) 
    lev_350  = Column(Float) 
    lev_400  = Column(Float) 
    lev_450  = Column(Float) 
    lev_500  = Column(Float) 
    lev_550  = Column(Float) 
    lev_600  = Column(Float) 
    lev_650  = Column(Float) 
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaUE_AVG(Base):
    __tablename__ = 'ue_avg'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_100  = Column(Float) 
    lev_150  = Column(Float) 
    lev_200  = Column(Float) 
    lev_250  = Column(Float) 
    lev_300  = Column(Float) 
    lev_350  = Column(Float) 
    lev_400  = Column(Float) 
    lev_450  = Column(Float) 
    lev_500  = Column(Float) 
    lev_550  = Column(Float) 
    lev_600  = Column(Float) 
    lev_650  = Column(Float) 
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaVE_AVG(Base):
    __tablename__ = 've_avg'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_100  = Column(Float) 
    lev_150  = Column(Float) 
    lev_200  = Column(Float) 
    lev_250  = Column(Float) 
    lev_300  = Column(Float) 
    lev_350  = Column(Float) 
    lev_400  = Column(Float) 
    lev_450  = Column(Float) 
    lev_500  = Column(Float) 
    lev_550  = Column(Float) 
    lev_600  = Column(Float) 
    lev_650  = Column(Float) 
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaW(Base):
    __tablename__ = 'w'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_100  = Column(Float) 
    lev_150  = Column(Float) 
    lev_200  = Column(Float) 
    lev_250  = Column(Float) 
    lev_300  = Column(Float) 
    lev_350  = Column(Float) 
    lev_400  = Column(Float) 
    lev_450  = Column(Float) 
    lev_500  = Column(Float) 
    lev_550  = Column(Float) 
    lev_600  = Column(Float) 
    lev_650  = Column(Float) 
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaRH(Base):
    __tablename__ = 'rh'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_100  = Column(Float) 
    lev_150  = Column(Float) 
    lev_200  = Column(Float) 
    lev_250  = Column(Float) 
    lev_300  = Column(Float) 
    lev_350  = Column(Float) 
    lev_400  = Column(Float) 
    lev_450  = Column(Float) 
    lev_500  = Column(Float) 
    lev_550  = Column(Float) 
    lev_600  = Column(Float) 
    lev_650  = Column(Float) 
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaGEO(Base):
    __tablename__ = 'geo'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_100  = Column(Float) 
    lev_150  = Column(Float) 
    lev_200  = Column(Float) 
    lev_250  = Column(Float) 
    lev_300  = Column(Float) 
    lev_350  = Column(Float) 
    lev_400  = Column(Float) 
    lev_450  = Column(Float) 
    lev_500  = Column(Float) 
    lev_550  = Column(Float) 
    lev_600  = Column(Float) 
    lev_650  = Column(Float) 
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaCLOUD(Base):
    __tablename__ = 'cloud'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    lev_100  = Column(Float) 
    lev_150  = Column(Float) 
    lev_200  = Column(Float) 
    lev_250  = Column(Float) 
    lev_300  = Column(Float) 
    lev_350  = Column(Float) 
    lev_400  = Column(Float) 
    lev_450  = Column(Float) 
    lev_500  = Column(Float) 
    lev_550  = Column(Float) 
    lev_600  = Column(Float) 
    lev_650  = Column(Float) 
    lev_700  = Column(Float) 
    lev_750  = Column(Float) 
    lev_800  = Column(Float) 
    lev_850  = Column(Float) 
    lev_900  = Column(Float) 
    lev_925  = Column(Float) 
    lev_1000  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaPRECIP(Base):
    __tablename__ = 'precip'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaACCCON(Base):
    __tablename__ = 'acccon'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaSFC_PRESS(Base):
    __tablename__ = 'sfc_press'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaSEA_PRESS(Base):
    __tablename__ = 'sea_press'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaT2MJ(Base):
    __tablename__ = 't2mj'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaTD2MJ(Base):
    __tablename__ = 'td2mj'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaU10MJ(Base):
    __tablename__ = 'u10mj'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaV10MJ(Base):
    __tablename__ = 'v10mj'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaLE(Base):
    __tablename__ = 'le'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaH(Base):
    __tablename__ = 'h'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaRSHORT(Base):
    __tablename__ = 'rshort'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaRLONG(Base):
    __tablename__ = 'rlong'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaRLONGUP(Base):
    __tablename__ = 'rlongup'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    value  = Column(Float) 
    point_gid = Column(Integer, ForeignKey('points.gid'))



Base.metadata.create_all(engine)


def clear_tables():
    talbes = [
        CempaSMOIST1,
        CempaSMOIST2,
        CempaSMOIST3,
        CempaSMOIST4,
        CempaALBEDT,
        CempaTEMPC,
        CempaUE_AVG,
        CempaVE_AVG,
        CempaW,
        CempaRH,
        CempaGEO,
        CempaCLOUD,
        CempaPRECIP,
        CempaACCCON,
        CempaSFC_PRESS,
        CempaSEA_PRESS,
        CempaT2MJ,
        CempaTD2MJ,
        CempaU10MJ,
        CempaV10MJ,
        CempaLE,
        CempaH,
        CempaRSHORT,
        CempaRLONG,
        CempaRLONGUP,
    ]
    for table in talbes:
        # TODO Deletar via trucade reset gid
        session = create_session()
        session.execute(delete(table).where(table.gid > 0))
        session.execute(
            f'ALTER SEQUENCE {table.__tablename__}_gid_seq RESTART WITH 1'
        )
        session.commit()
