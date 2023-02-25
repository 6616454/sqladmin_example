from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.infrastructure.db.client import DatabaseClient


def db_provider() -> None:
    raise NotImplementedError


class DBProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self._pool = pool

    async def provide_db(self):
        async with self._pool() as session:
            yield DatabaseClient(session)
