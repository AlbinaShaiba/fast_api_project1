from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.testing.pickleable import User

from src.core.database import Base, array_or_none_an
from src.core.models.comment import Comment
from src.core.sql_enums import StatusPost


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, auto_increment=True)
    title: Mapped[str]
    text: Mapped[str]
    main_photo_url = Mapped[str]
    photos_url = Mapped[array_or_none_an]
    status = Mapped[StatusPost] = mapped_column(default=StatusPost.PUBLISHED,
                                                server_default=text('"DRAFT"'))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    user: Mapped['User'] = relationship(
        'User',
        back_populates='posts'
    )
    comments: Mapped[list['Comment']] = relationship(
        'Comment',
        back_populates='post',
        cascade='all, delete-orphan'
    )
