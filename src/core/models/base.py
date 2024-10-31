from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)