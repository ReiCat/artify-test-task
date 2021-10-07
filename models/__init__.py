from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, BigInteger


Base = declarative_base()


class AbstractBase(Base):
    __abstract__ = True

    id = Column(BigInteger, primary_key=True, autoincrement=True)


class AbstractDateTimeBase(AbstractBase):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    instance = model(**kwargs)
    session.add(instance)
    session.commit()
    return instance, True
