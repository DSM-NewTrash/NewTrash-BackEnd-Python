from sqlalchemy import Column, VARCHAR, INTEGER

from server.core import Base


class Badge(Base):
    __tablename__ = 'tbl_badge'

    id = Column('id', INTEGER, autoincrement=True, primary_key=True)
    name = Column('name', VARCHAR(7), nullable=True)
    path = Column('path', VARCHAR(360), nullable=True)
