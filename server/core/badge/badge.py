from sqlalchemy import Column, VARCHAR, INTEGER

from server.core import Base


class Badge(Base):
    __tablename__ = 'tbl_badge'

    level = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(7), nullable=True)
    path = Column(VARCHAR(360), nullable=True)
