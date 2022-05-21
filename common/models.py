import datetime
import uuid

from sqlalchemy import Column, Date, DateTime


def generate_uuid():
    return uuid.uuid4()


def generate_current_date():
    return datetime.date.today().strftime("%Y-%m-%d")


def generate_current_datetime():
    return datetime.datetime.today()


class CreateDateMixin:
    created_at = Column(Date, default=generate_current_date)


class UpdateDateMixin:
    updated_at = Column(Date, default=generate_current_date, onupdate=generate_current_date)


class LoginUserDateMixin(UpdateDateMixin):
    updated_at = Column(DateTime, default=generate_current_date, onupdate=generate_current_datetime)
    login = Column(DateTime, nullable=False)
