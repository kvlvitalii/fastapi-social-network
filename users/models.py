from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from common.models import CreateDateMixin, LoginUserDateMixin, IdMixin
from settings import Base


class UserModel(Base, IdMixin, CreateDateMixin):
    __tablename__ = "users"

    password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)


class UserLogsModel(Base, IdMixin, LoginUserDateMixin):
    __tablename__ = "userlogs"

    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    user = relationship("UserModel", backref="logs", uselist=False)
    request_url = Column(String)
