from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from src.infrastructure.db.config import DBConfig


def create_engine(db_config: DBConfig) -> AsyncEngine:
    return create_async_engine(url=db_config.database_url, echo=db_config.echo)


def create_pool(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
