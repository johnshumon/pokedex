"""Translated pokemon module"""

from typing import Any

from fastapi import APIRouter, Response, status

from app.utils.async_client import fetch
from app.utils.translation import translate
from app.utils.translation_type import TranslationType

router = APIRouter()


@router.get("")
async def get_translated_pokemon(pokemon_name: str, response: Response) -> Any:
    """Handler for getting a translated pokemon"""

    query_result = await fetch(pokemon_name)

    if query_result["status_code"] == 404:
        response.status_code = status.HTTP_404_NOT_FOUND
        return query_result

    query_result = query_result["message"]

    # set values for result
    name = query_result["name"]
    habitat = query_result["habitat"]["name"]
    is_legendary = query_result["is_legendary"]

    # Translation rules:
    # > Yoda translation: only if habitat is 'cave'
    #   or it's a legendary Pokemon
    # > Shakespeare translation: to all other pokemon
    # -----------------------------------------------
    if habitat == "cave" or is_legendary is True:
        description = query_result["flavor_text_entries"][0]["flavor_text"]
        translated_desc = await translate(description, TranslationType.YODA.name)
    else:
        description = query_result["flavor_text_entries"][0]["flavor_text"]
        translated_desc = await translate(description, TranslationType.SHAKESPEARE.name)

    result = {
        "name": name,
        "description": translated_desc,
        "habitat": habitat,
        "isLegendary": is_legendary,
    }

    return result
