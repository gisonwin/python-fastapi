from db.database import Base
from sqlalchemy import Column, String, DateTime, func, Integer


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    password = Column(String(32), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ShortUrl(Base):
    __tablename__ = 'short_url'
    id = Column(Integer, primary_key=True, autoincrement=True)
    short_tag = Column(String(20), nullable=False)
    short_url = Column(String(20), nullable=False)
    long_url = Column(String, nullable=False)
    visits_count = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    created_by = Column(String(20), nullable=False)
    msg_context = Column(String, nullable=False)
