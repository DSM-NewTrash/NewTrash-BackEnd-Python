from server.core import session_scope
from fastapi import APIRouter

from ..core.user.schema.auth import SignUp, Login
from ..utill.auth import create_user, logins, check_id

app = APIRouter(prefix="/users")


@app.post("")
async def sign_up(body: SignUp):
    with session_scope() as session:
        return create_user(session=session, body=body)


@app.post("/login")
async def login(body: Login):
    with session_scope() as session:
        return logins(session=session, body=body)


@app.get("/{user_id}")
async def check_ids(user_id: str):
    with session_scope() as session:
        return check_id(session=session, user_id=user_id)
