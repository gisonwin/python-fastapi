from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

async_engine = create_async_engine('mysql+aiomysql://root:root@localhost:3306/hq', echo=True)

Base = declarative_base()

session_local = sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)
