from fastapi import Depends

from src.business_logic.services.posts_get import PostsGetService
from src.infrastructure.db.client import DatabaseClient
from src.presentation.api.di.providers.db import db_provider


def posts_get_service(db_client: DatabaseClient = Depends(db_provider)) -> PostsGetService:
    return PostsGetService(db_client)
