"""Application routes"""

from fastapi import APIRouter

from app.apis.v1.handlers import home
from app.apis.v1.handlers import pokemon

api_router = APIRouter()
api_router.include_router(home.router, prefix="/home")
api_router.include_router(pokemon.router, prefix="/pokemon/{pokemon_name}")
