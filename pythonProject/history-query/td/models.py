import datetime
from sqlalchemy import String, Integer, Date, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class DataBlock(Base):
    __tablename__ = 's_datablock'
    sd_stime: Mapped[datetime.datetime] = mapped_column(Date, primary_key=True)
    sd_itime: Mapped[datetime.datetime] = mapped_column(Date, comment='记录插入时间')
    sd_bin: Mapped[str] = mapped_column(String)
    sd_len: Mapped[int] = mapped_column(Integer)
    sd_dsrc: Mapped[str] = mapped_column(String)
    sd_guid: Mapped[int] = mapped_column(Integer)
    sd_framecnt: Mapped[int] = mapped_column(Integer)
    sd_startime: Mapped[int] = mapped_column(Integer)
    sd_flag: Mapped[int] = mapped_column(Integer)
    sd_crcresult: Mapped[int] = mapped_column(Integer)
    devcode: Mapped[str] = mapped_column(String)
    devchannel: Mapped[str] = mapped_column(String)
    satellite_id: Mapped[int] = mapped_column(Integer, nullable=False, comment='TAG')


class Meters(Base):
    __tablename__ = 'meters'
    ts: Mapped[datetime.datetime] = mapped_column(Date, primary_key=True)
    current: Mapped[float] = mapped_column(Float(12, False, 5))
    phase: Mapped[float] = mapped_column(Float(12).decimal_return_scale)
    location: Mapped[str] = mapped_column(String(64), comment='TAG')
    groupid: Mapped[int] = mapped_column(Integer, nullable=False, comment='TAG')
