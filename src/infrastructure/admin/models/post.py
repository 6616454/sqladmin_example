from sqladmin import ModelView

from src.infrastructure.db.models.post import Post


class PostAdmin(ModelView, model=Post):
    pass
