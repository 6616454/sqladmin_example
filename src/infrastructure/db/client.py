from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession


class DatabaseClient:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def __aenter__(self) -> "DatabaseClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.rollback()
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def execute(self, statement) -> Any:
        return await self._session.execute(statement)
