import boto3
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

from starlette import status

from server.config import SECURITY
from jose import JWTError, jwt

from server.core import session_scope
from server.core.user.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(user_id: str):
    exp = datetime.utcnow() + timedelta(days=30)
    encoded_jwt = jwt.encode({"exp": exp, "sub": user_id}, SECURITY.SECRET_KEY, algorithm=['HS256'])
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    with session_scope() as session:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
        try:
            payload = jwt.decode(token, SECURITY.SECRET_KEY, algorithms=['HS256'])
            user_id: str = payload.get("sub")
            if user_id is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        return user_id


def s3_connection():
    s3 = boto3.client('s3', aws_access_key_id=SECURITY.aws_access_key,
                      aws_secret_access_key=SECURITY.aws_secret_key,
                      region_name=SECURITY.region)
    return s3
