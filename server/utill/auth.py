from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..core.user.schema.auth import SignUp, Login, Certification
from ..core.user.user import User
from ..utill.security import get_password_hash, verify_password, create_access_token


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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not verify_password(plain_password=body.password, hashed_password=user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return {
        "access_token": create_access_token(user_id=user.id)
    }


def is_certification(session: Session, body: Certification, user_id: str):
    user = session.query(User).filter_by(id=user_id).first()
    user.certificate = body.certificate
    user.is_certificate = True
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="success")
