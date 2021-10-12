from sqlalchemy import *
from migrate import *

from models.user import User


def upgrade(migrate_engine):
    User.__table__.create(migrate_engine)


def downgrade(migrate_engine):
    User.__table__.drop(migrate_engine)
