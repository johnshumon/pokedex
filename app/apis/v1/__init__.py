"""Application routes"""

from fastapi import APIRouter

from app.apis.v1.handlers import home

api_router = APIRouter()
api_router.include_router(home.router, prefix="/home")
