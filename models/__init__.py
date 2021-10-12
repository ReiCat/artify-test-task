from datetime import datetime

# from sqlalchemy.ext.declarative import declarative_base
from tornado_sqlalchemy import declarative_base
from sqlalchemy import Column, DateTime, BigInteger


Base = declarative_base()


class AbstractBase(Base):
    __abstract__ = True

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    def as_dict(self):
        return {column.key: getattr(self, attr) for attr, column in self.__mapper__.c.items()}


class AbstractDateTimeBase(AbstractBase):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)