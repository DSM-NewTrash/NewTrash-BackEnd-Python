from server.core import session_scope
from fastapi import APIRouter, Depends, status

from ..core.user.schema.auth import SignUp, Login, Certification
from ..utill.auth import create_user, logins, is_certification, quiz_count, get_exp_badge, get_profile
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
async def certification(body: Certification, user: str = Depends(get_current_user)):
    with session_scope() as session:
        return is_certification(session=session, body=body, user_id=user)


@app.get("/quizs", status_code=status.HTTP_200_OK)
async def get_quiz_count(user: str = Depends(get_current_user)):
    with session_scope() as session:
        return quiz_count(session=session, user_id=user)


@app.get("/", status_code=status.HTTP_200_OK)
async def exp_badge(user: str = Depends(get_current_user)):
    with session_scope() as session:
        return get_exp_badge(session=session, user_id=user)


@app.get("/profile", status_code=status.HTTP_200_OK)
async def profile(user: str = Depends(get_current_user)):
    with session_scope() as session:
        return get_profile(session=session, user_id=user)


# @app.patch("/profile", status_code=status.HTTP_204_NO_CONTENT)
# async def profile(user: str = Depends(get_current_user)):
#     with session_scope() as session:
#         return
