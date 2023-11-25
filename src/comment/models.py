from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean

from auth.models import user

metadata = MetaData()

comment = Table(
    'comment',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('content', String),
    Column('user_id', Integer, ForeignKey(user.c.id)),
    Column('at_date', TIMESTAMP, default=datetime.utcnow),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)
