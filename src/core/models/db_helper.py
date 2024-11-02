from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.core.config import settings


class DatabaseHelper:
    def __init__(self,
                 url: str):

        self.engine = create_async_engine(url=url)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine)

async def dispose(self):
    await self.engine.dispose()

async def session_getter(self):
    async with self.session_factory() as session:
        yield session
        await session.close()

db_helper = DatabaseHelper(
    url=str(settings.db.url))