from datetime import datetime

from geoalchemy2 import Geometry
from numpy import delete
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import DateTime, Float, Integer, String
from sqlalchemy import delete

from cempa.db import Base, engine, create_session


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


class CempaALBEDT(Base):
    __tablename__ = 'albedt'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    albedt = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaTEMPC(Base):
    __tablename__ = 'tempc'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    tempc_01 = Column(Float)
    tempc_02 = Column(Float)
    tempc_03 = Column(Float)
    tempc_04 = Column(Float)
    tempc_05 = Column(Float)
    tempc_06 = Column(Float)
    tempc_07 = Column(Float)
    tempc_08 = Column(Float)
    tempc_09 = Column(Float)
    tempc_10 = Column(Float)
    tempc_11 = Column(Float)
    tempc_12 = Column(Float)
    tempc_13 = Column(Float)
    tempc_14 = Column(Float)
    tempc_15 = Column(Float)
    tempc_16 = Column(Float)
    tempc_17 = Column(Float)
    tempc_18 = Column(Float)
    tempc_19 = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaUE_AVG(Base):
    __tablename__ = 'ue_avg'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    ue_avg_01 = Column(Float)
    ue_avg_02 = Column(Float)
    ue_avg_03 = Column(Float)
    ue_avg_04 = Column(Float)
    ue_avg_05 = Column(Float)
    ue_avg_06 = Column(Float)
    ue_avg_07 = Column(Float)
    ue_avg_08 = Column(Float)
    ue_avg_09 = Column(Float)
    ue_avg_10 = Column(Float)
    ue_avg_11 = Column(Float)
    ue_avg_12 = Column(Float)
    ue_avg_13 = Column(Float)
    ue_avg_14 = Column(Float)
    ue_avg_15 = Column(Float)
    ue_avg_16 = Column(Float)
    ue_avg_17 = Column(Float)
    ue_avg_18 = Column(Float)
    ue_avg_19 = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaVE_AVG(Base):
    __tablename__ = 've_avg'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    ve_avg_01 = Column(Float)
    ve_avg_02 = Column(Float)
    ve_avg_03 = Column(Float)
    ve_avg_04 = Column(Float)
    ve_avg_05 = Column(Float)
    ve_avg_06 = Column(Float)
    ve_avg_07 = Column(Float)
    ve_avg_08 = Column(Float)
    ve_avg_09 = Column(Float)
    ve_avg_10 = Column(Float)
    ve_avg_11 = Column(Float)
    ve_avg_12 = Column(Float)
    ve_avg_13 = Column(Float)
    ve_avg_14 = Column(Float)
    ve_avg_15 = Column(Float)
    ve_avg_16 = Column(Float)
    ve_avg_17 = Column(Float)
    ve_avg_18 = Column(Float)
    ve_avg_19 = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaW(Base):
    __tablename__ = 'w'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    w_01 = Column(Float)
    w_02 = Column(Float)
    w_03 = Column(Float)
    w_04 = Column(Float)
    w_05 = Column(Float)
    w_06 = Column(Float)
    w_07 = Column(Float)
    w_08 = Column(Float)
    w_09 = Column(Float)
    w_10 = Column(Float)
    w_11 = Column(Float)
    w_12 = Column(Float)
    w_13 = Column(Float)
    w_14 = Column(Float)
    w_15 = Column(Float)
    w_16 = Column(Float)
    w_17 = Column(Float)
    w_18 = Column(Float)
    w_19 = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaRH(Base):
    __tablename__ = 'rh'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    rh_01 = Column(Float)
    rh_02 = Column(Float)
    rh_03 = Column(Float)
    rh_04 = Column(Float)
    rh_05 = Column(Float)
    rh_06 = Column(Float)
    rh_07 = Column(Float)
    rh_08 = Column(Float)
    rh_09 = Column(Float)
    rh_10 = Column(Float)
    rh_11 = Column(Float)
    rh_12 = Column(Float)
    rh_13 = Column(Float)
    rh_14 = Column(Float)
    rh_15 = Column(Float)
    rh_16 = Column(Float)
    rh_17 = Column(Float)
    rh_18 = Column(Float)
    rh_19 = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaGEO(Base):
    __tablename__ = 'geo'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    geo_01 = Column(Float)
    geo_02 = Column(Float)
    geo_03 = Column(Float)
    geo_04 = Column(Float)
    geo_05 = Column(Float)
    geo_06 = Column(Float)
    geo_07 = Column(Float)
    geo_08 = Column(Float)
    geo_09 = Column(Float)
    geo_10 = Column(Float)
    geo_11 = Column(Float)
    geo_12 = Column(Float)
    geo_13 = Column(Float)
    geo_14 = Column(Float)
    geo_15 = Column(Float)
    geo_16 = Column(Float)
    geo_17 = Column(Float)
    geo_18 = Column(Float)
    geo_19 = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaCLOUD(Base):
    __tablename__ = 'cloud'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    cloud_01 = Column(Float)
    cloud_02 = Column(Float)
    cloud_03 = Column(Float)
    cloud_04 = Column(Float)
    cloud_05 = Column(Float)
    cloud_06 = Column(Float)
    cloud_07 = Column(Float)
    cloud_08 = Column(Float)
    cloud_09 = Column(Float)
    cloud_10 = Column(Float)
    cloud_11 = Column(Float)
    cloud_12 = Column(Float)
    cloud_13 = Column(Float)
    cloud_14 = Column(Float)
    cloud_15 = Column(Float)
    cloud_16 = Column(Float)
    cloud_17 = Column(Float)
    cloud_18 = Column(Float)
    cloud_19 = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaPRECIP(Base):
    __tablename__ = 'precip'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    precip = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaACCCON(Base):
    __tablename__ = 'acccon'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    acccon = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaSFC_PRESS(Base):
    __tablename__ = 'sfc_press'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    sfc_press = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaSEA_PRESS(Base):
    __tablename__ = 'sea_press'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    sea_press = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaT2MJ(Base):
    __tablename__ = 't2mj'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    t2mj = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaTD2MJ(Base):
    __tablename__ = 'td2mj'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    td2mj = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaU10MJ(Base):
    __tablename__ = 'u10mj'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    u10mj = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaV10MJ(Base):
    __tablename__ = 'v10mj'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    v10mj = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaLE(Base):
    __tablename__ = 'le'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    le = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaH(Base):
    __tablename__ = 'h'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    h = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaRSHORT(Base):
    __tablename__ = 'rshort'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    rshort = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaRLONG(Base):
    __tablename__ = 'rlong'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    rlong = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


class CempaRLONGUP(Base):
    __tablename__ = 'rlongup'
    gid = Column(Integer, primary_key=True)
    datetime = Column(DateTime, index=True)
    rlongup = Column(Float)
    point_gid = Column(Integer, ForeignKey('points.gid'))


Base.metadata.create_all(engine)


def clear_tables():
    talbes = [
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
        session = create_session()
        session.execute(delete(table).where(table.gid > 0))
        session.commit()
