from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(default=db.func.current_timestamp())

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
