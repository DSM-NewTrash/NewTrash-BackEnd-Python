from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

from server.config import SECURITY
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(user_id: str):
    exp = datetime.utcnow() + timedelta(minutes=1000000000)
    encoded_jwt = jwt.encode({"exp": exp, "sub": user_id}, SECURITY.SECRET_KEY, algorithm='HS256')
    return encoded_jwt
