from sqlalchemy import text, JSON
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.core.database import array_or_none_an
from src.core.sql_enums import GenderEnum, ProfessionEnum

from src.core.models.base import Base


class Profile(Base):
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    age: Mapped[int]
    gender: Mapped[GenderEnum]
    profession: Mapped[ProfessionEnum] = mapped_column(
        default=ProfessionEnum.DEVELOPER,
        server_default=text('"UNEMPLOYED"'),
    )
    interests: Mapped[array_or_none_an]
    contacts: Mapped[dict | None] = mapped_column(JSON)
    user: Mapped['User'] = relationship(
        'User',
        back_populates='profile',
        uselist=False
    )