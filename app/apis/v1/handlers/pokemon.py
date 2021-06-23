"""Pokemon module"""

from typing import Any

from fastapi import APIRouter, Response, status

from app.utils.async_client import fetch

router = APIRouter()


@router.get("")
async def get_pokemon(pokemon_name: str, response: Response) -> Any:
    """Handler for getting details of a pokemon"""

    query_result = await fetch(pokemon_name)

    if query_result["status_code"] == 404:
        response.status_code = status.HTTP_404_NOT_FOUND
        return query_result

    query_result = query_result["message"]

    # set values for result
    name = query_result["name"]
    description = query_result["flavor_text_entries"][0]["flavor_text"]
    habitat = query_result["habitat"]["name"]
    is_legendary = query_result["is_legendary"]

    result = {
        "name": name,
        "description": description,
        "habitat": habitat,
        "isLegendary": is_legendary,
    }
    return result
