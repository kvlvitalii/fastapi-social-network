from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from common.models import CreateDateMixin, generate_uuid, LoginUserDateMixin
from settings import Base


class UserModel(Base, CreateDateMixin):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)


class UserLogsModel(Base, LoginUserDateMixin):
    __tablename__ = "userlogs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    user = relationship('UserModel', backref='logs', uselist=False)
    request_url = Column(String)
