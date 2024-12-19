from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from config.config import get_settings

async_engine = create_async_engine(get_settings().ASYNC_DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)
