from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..core.user.schema.market import Market
from ..core.user.user import User


def market(session: Session, body: Market, user_id: str):
    user = session.query(User).filter_by(id=user_id).first()
    if user.point - body.point < 0:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough points")
    user.point = user.point - body.point
    return HTTPException(status_code=status.HTTP_200_OK, detail="success")
