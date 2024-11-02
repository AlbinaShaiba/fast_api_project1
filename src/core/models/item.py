from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from src.core.database import Base


class Item(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, auto_increment=True)
    name: str = mapped_column(String)
    description: str = mapped_column(String)
    price: int = mapped_column(Integer)
