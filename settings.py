from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_USERNAME_US, DB_PASSWORD_US, DB_HOST_US, DB_PORT_US, DB_NAME_US

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USERNAME_US}:{DB_PASSWORD_US}@{DB_HOST_US}:{DB_PORT_US}/{DB_NAME_US}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
