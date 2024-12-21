from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[str] = mapped_column(default=db.func.current_timestamp())
