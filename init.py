import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Index
from sqlalchemy.exc import ProgrammingError
from sqlalchemy_utils import create_database, database_exists

from models import Base

def create_index(index, engine):
    try:
        index.create(bind=engine)
    except ProgrammingError as _:
        pass

def initialize():
    dsn = os.environ.get("DATABASE_URL")
    engine = create_engine(dsn, echo=False)
    if not database_exists(engine.url):
        create_database(dsn)
    Base.metadata.create_all(engine)