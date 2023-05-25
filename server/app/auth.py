from server.core import session_scope
from fastapi import APIRouter, Depends

from ..core.user.schema.auth import SignUp, Login, Certification
from ..core.user.user import User
from ..utill.auth import create_user, logins, is_certification
from ..utill.security import get_current_user

app = APIRouter(prefix="/users")


@app.post("")
async def sign_up(body: SignUp):
    with session_scope() as session:
        return create_user(session=session, body=body)


@app.post("/login")
async def login(body: Login):
    with session_scope() as session:
        return logins(session=session, body=body)


@app.post("/profile")
async def login(body: Certification, user: User = Depends(get_current_user)):
    with session_scope() as session:
        return is_certification(session=session, body=body, user=user)

