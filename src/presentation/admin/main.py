from fastapi import FastAPI
from sqladmin import Admin
from sqlalchemy.ext.asyncio import AsyncEngine

from src.infrastructure.admin import setup_admin_models


def build_admin_app(app: FastAPI, engine: AsyncEngine):
    admin_app = Admin(app=app, engine=engine)

    setup_admin_models(admin_app)

    return admin_app
