from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..core.user.schema.auth import SignUp, Login, Certification, Profile
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


def get_exp_badge(session: Session, user_id: str):
    user = session.query(User).filter(User.id == user_id).first()
    badge = session.query(Badge).filter(Badge.level == user.badge_id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {
        "nickname": user.nickname,
        "level": user.badge_id,
        "badge_image": f"https://new-trash.s3.ap-northeast-2.amazonaws.com/badge/{user.badge_id}.png",
        "exp": user.exp,
        "max_exp": max_exp[user.badge_id],
        "point": user.point
    }


def get_profile(session: Session, user_id: str):
    user = session.query(User).filter(User.id == user_id).first()
    badge = session.query(Badge).filter(Badge.level == user.badge_id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {
        "id": user.id,
        "nickname": user.nickname,
        "profile": user.profile,
        "introduce": user.introduce,
        "level": user.badge_id,
        "badge": badge.name,
        "badge_image": f"https://new-trash.s3.ap-northeast-2.amazonaws.com/badge/mypage/{user.badge_id}.png",
        "exp": user.exp,
        "point": user.point,
        "certificate": user.certificate,
        "is_certificate": user.is_certificate
    }


def update_profile(session: Session, body: Profile, user_id: str):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if body.profile:
        user.profile = body.profile
    if body.nickname:
        user.nickname = body.nickname
    if body.introduce:
        user.introduce = body.introduce

    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
