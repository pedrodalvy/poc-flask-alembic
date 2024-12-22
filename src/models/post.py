from sqlalchemy import ForeignKey
from src.models.base import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(default=db.func.current_timestamp())
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship("User", back_populates="posts")
