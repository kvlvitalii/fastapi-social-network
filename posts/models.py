from sqlalchemy import Column, String, ForeignKey, Text, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from common.models import CreateDateMixin, UpdateDateMixin, IdMixin
from settings import Base


class PostModel(Base, IdMixin, CreateDateMixin, UpdateDateMixin):
    __tablename__ = "posts"

    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    user = relationship("UserModel", backref="posts")
    header = Column(String, nullable=False, unique=True)
    text = Column(Text, nullable=True, default="")
    is_active = Column(Boolean, default=True)


class PostLikeModel(Base, IdMixin, CreateDateMixin):
    __tablename__ = "likes"

    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    post_id = Column(UUID, ForeignKey("posts.id"), nullable=False)
    user = relationship("UserModel", backref="likes")
    post = relationship("PostModel", backref="likes")
    __table_args__ = (UniqueConstraint("user_id", "post_id", name="_user_posts_like"),)
