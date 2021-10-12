from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

from . import AbstractBase


class Sector(AbstractBase):
    __tablename__ = 'sectors'
    
    name = Column(String(50), nullable=False)
