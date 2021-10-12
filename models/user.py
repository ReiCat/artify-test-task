from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean

from . import AbstractBase


class User(AbstractBase):
    __tablename__ = 'users'
    
    name = Column(String(50), nullable=False)
    selected_sectors = Column(String(300))
    agreed_to_terms = Column(Boolean, default=False)
