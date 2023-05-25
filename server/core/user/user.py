from server.core import Base

from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey, Boolean


class User(Base):
    __tablename__ = 'tbl_user'

    id = Column(VARCHAR(12), primary_key=True)
    nickname = Column(VARCHAR(12), nullable=False)
    password = Column(VARCHAR(60), nullable=False)
    profile = Column(VARCHAR(360), default=" ")
    point = Column(INTEGER, default=0)
    introduce = Column(VARCHAR(30), nullable=False, default='')
    quiz_limit_count = Column(INTEGER, default=0)
    exp = Column(INTEGER, default=0)
    is_certificate = Column(Boolean, default=False)
    badge_id = Column(INTEGER, ForeignKey('tbl_badge.level'), default=1)