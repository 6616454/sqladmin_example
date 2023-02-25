from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


class DatabaseClient:
    def __init__(self, pool: async_sessionmaker[AsyncSession]) -> None:
        self._pool = pool

    async def __aenter__(self) -> "DatabaseClient":
        self._session: AsyncSession = self._pool()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def execute(self, statement: str, **params) -> Any:
        return await self._session.execute(text(statement), params)
