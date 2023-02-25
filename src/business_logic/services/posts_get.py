from sqlalchemy import select

from src.business_logic.dto.post import PostDTO
from src.infrastructure.db.client import DatabaseClient
from src.infrastructure.db.models.post import Post


class PostsGetService:
    def __init__(self, db_client: DatabaseClient):
        self.db_client = db_client

    async def execute(self) -> list[PostDTO]:
        async with self.db_client as db:
            statement = select(Post)

            return (await db.execute(statement)).scalars().all()
