from fastapi import APIRouter
from . import auth, image, market

api_router = APIRouter()

api_router.include_router(auth.app, tags=['auth'])
api_router.include_router(image.app, tags=['image'])
api_router.include_router(market.app, tags=['market'])
