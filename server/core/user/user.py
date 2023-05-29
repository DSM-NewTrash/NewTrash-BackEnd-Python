from server.core import Base
from server.core.badge.badge import Badge
from server.config import SECURITY

from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey, Boolean


class User(Base):
    __tablename__ = 'tbl_user'

    id = Column(VARCHAR(12), primary_key=True)
    nickname = Column(VARCHAR(12), nullable=False)
    password = Column(VARCHAR(60), nullable=False)
    profile = Column(VARCHAR(360), default=SECURITY.user_default_image)
    point = Column(INTEGER, default=0)
    introduce = Column(VARCHAR(30), nullable=False, default='')
    quiz_limit_count = Column(INTEGER, default=80)
    exp = Column(INTEGER, default=0)
    certificate = Column(VARCHAR(255), nullable=True)
    is_certificate = Column(Boolean)
    badge_id = Column(INTEGER, ForeignKey('tbl_badge.level'), default=1)