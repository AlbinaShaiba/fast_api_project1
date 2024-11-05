from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base, uniq_str_an
from src.core.models.comment import Comment
from src.core.models.post import Post
from src.core.models.profile import Profile


class User(Base):
    username: Mapped[uniq_str_an]
    email: Mapped[uniq_str_an]
    password: Mapped[str]
    posts: Mapped[list['Post']] = relationship(
        'Post',
        back_populates='author',
        cascade='all, delete-orphan'
    )
    profile: Mapped['Profile'] = relationship(
        'Profile',
        back_populates='user',
        cascade='all, delete, delete-orphan',
        lazy='joined'
    )
    comments: Mapped[list['Comment']] = relationship(
        'Comment',
        back_populates='author',
        cascade='all, delete-orphan'
    )

