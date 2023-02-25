from src.infrastructure.db.client import DatabaseClient


class PostsGetService:
    def __init__(self, db_client: DatabaseClient):
        self.db_client = db_client

    async def execute(self):
        async with self.db_client as db:
            statement = """SELECT * FROM posts"""

            return await db.execute(statement)
