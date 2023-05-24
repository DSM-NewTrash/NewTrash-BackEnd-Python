from fastapi import FastAPI

import uvicorn

from server.app import api_router

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from server.config import MySQL

engine = create_engine(
    url=MySQL.MY_SQL_URL,

)

Base = declarative_base()


def create_all_table():
    from server.core.badge.badge import Badge
    from server.core.user.user import User

    Base.metadata.create_all(bind=engine)


app = FastAPI()
create_all_table()
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
