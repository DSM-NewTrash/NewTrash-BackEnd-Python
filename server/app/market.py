from typing import List

from server.core import session_scope
from fastapi import APIRouter, Depends

from ..core.user.schema.market import Market
from ..utill.security import get_current_user
from server.utill.market import market

app = APIRouter(prefix="/markets")


@app.post("/point")
async def markets(body: Market, user: str = Depends(get_current_user)):
    with session_scope() as session:
        return market(session=session, user_id=user, body=body)
