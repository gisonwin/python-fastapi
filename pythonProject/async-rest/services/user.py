from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.model import User
from db.database import async_engine, Base


class UserService:
    @staticmethod
    async def get_user(async_session: AsyncSession, user_id: int):
        result = await async_session.execute(select(User).where(User.id == user_id))
        return result.scalars().first()
