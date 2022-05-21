from sqlalchemy import Column, String, ForeignKey, Text, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from common.models import CreateDateMixin, UpdateDateMixin, generate_uuid
from settings import Base


class PostModel(Base, CreateDateMixin, UpdateDateMixin):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    user = relationship("UserModel", backref="posts")
    header = Column(String, nullable=False, unique=True)
    text = Column(Text, nullable=True, default="")
    is_active = Column(Boolean, default=True)


class PostLikeModel(Base, CreateDateMixin):
    __tablename__ = "likes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    post_id = Column(UUID, ForeignKey("posts.id"), nullable=False)
    user = relationship("UserModel", backref="likes")
    post = relationship("PostModel", backref="likes")
    __table_args__ = (UniqueConstraint("user_id", "post_id", name="_user_posts_like"),)
