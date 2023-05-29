from fastapi import APIRouter
from . import auth, image

api_router = APIRouter()

api_router.include_router(auth.app, tags=['auth'])
api_router.include_router(image.app, tags=['image'])
