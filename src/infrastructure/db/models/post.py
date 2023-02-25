from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column()
