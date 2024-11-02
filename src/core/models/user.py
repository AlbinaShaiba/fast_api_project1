from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, auto_increment=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
