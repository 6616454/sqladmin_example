from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.presentation.api.di.providers.db import DBProvider, db_provider


def setup_di(app: FastAPI, pool: async_sessionmaker[AsyncSession]) -> None:
    database_provider = DBProvider(pool)

    app.dependency_overrides[db_provider] = database_provider.provide_db
