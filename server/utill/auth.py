from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..core.user.schema.auth import SignUp, Login, Certification
from ..core.user.user import User
from ..core.badge.badge import Badge
from ..utill.security import get_password_hash, verify_password, create_access_token

max_exp = [0, 1000, 3000, 8000, 15000, 28000]


def create_user(session: Session, body: SignUp):
    session.add(
        User(
            id=body.id,
            nickname=body.nickname,
            password=get_password_hash(body.password)
        )
    )

    return HTTPException(status_code=status.HTTP_201_CREATED, detail="success")


def logins(session: Session, body: Login):
    user = session.query(User).filter(User.id == body.id).first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not verify_password(plain_password=body.password, hashed_password=user.password):
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return {
        "access_token": create_access_token(user_id=user.id)
    }


def is_certification(session: Session, body: Certification, user_id: str):
    user = session.query(User).filter_by(id=user_id).first()
    user.certificate = body.certificate
    user.is_certificate = True
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="success")


def quiz_count(session: Session, user_id: str):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {
        "count": user.quiz_limit_count
    }


def get_profile(session: Session, user_id: str):
    user = session.query(User).filter(User.id == user_id).first()
    badge = session.query(Badge).filter(Badge.level == user.badge_id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {
        "nickname": user.nickname,
        "level": user.badge_id,
        "badge_image": badge.path,
        "exp": user.exp,
        "max_exp": max_exp[user.badge_id],
        "point": user.point
    }
