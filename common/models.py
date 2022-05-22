import datetime
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Date, DateTime


def generate_uuid():
    return uuid.uuid4()


def generate_current_date():
    return datetime.date.today().strftime("%Y-%m-%d")


def generate_current_datetime():
    return datetime.datetime.today()


class IdMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)


class CreateDateMixin:
    created_at = Column(Date, default=generate_current_date)


class UpdateDateMixin:
    updated_at = Column(
        Date, default=generate_current_date, onupdate=generate_current_date
    )


class LoginUserDateMixin:
    last_request_at = Column(
        DateTime, default=generate_current_date, onupdate=generate_current_datetime
    )
    last_login_at = Column(DateTime, nullable=False)
