from pydantic.v1 import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    ASYNC_DATABASE_URL: str = "sqlite+aiosqlite://short.db"
    TOKEN_SIGN_SECRECT: str = 'ZcjT6RcplyIFQoS7'


@lru_cache()
def get_settings():
    return Settings()
