"""Application routes"""

from fastapi import APIRouter

from app.apis.v1.handlers import home, pokemon, translated_pokemon

api_router = APIRouter()
api_router.include_router(home.router, prefix="/home")
api_router.include_router(pokemon.router, prefix="/pokemon/{pokemon_name}")
api_router.include_router(
    translated_pokemon.router, prefix="/pokemon/translated/{pokemon_name}"
)
