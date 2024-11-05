from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base
from src.core.models import User
from src.core.models.post import Post
from src.core.sql_enums import RatingEnum


class Comment(Base):
    text: Mapped[Text]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    is_published: Mapped[bool] = mapped_column(default=True, server_default=text('"false"'))
    rating: Mapped[RatingEnum] = mapped_column(default=RatingEnum.FIVE, server_default=text('"SEVEN"'))
    user: Mapped['User'] = relationship(
        'User',
        back_populates='comments'
    )
    post: Mapped['Post'] = relationship(
        'Post',
        back_populates='comments'
    )