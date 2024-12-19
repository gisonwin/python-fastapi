from fastapi import FastAPI, Depends
from db.database import async_engine, Base
from models.model import User, ShortUrl

app = FastAPI(title="FastAPI集成短链实战案例")


async def init_create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all(bind=conn))
        await conn.run_sync(Base.metadata.create_all(bind=conn))


@app.on_event("startup")
async def startup_event():
    await init_create_table()


@app.on_event("shutdown")
async def shutdown_event():
    pass
