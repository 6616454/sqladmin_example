from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import Base


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column()
