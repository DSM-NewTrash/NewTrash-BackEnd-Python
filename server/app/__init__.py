from fastapi import APIRouter
from . import auth

api_router = APIRouter()

api_router.include_router(auth.app, tags=['auth'])
