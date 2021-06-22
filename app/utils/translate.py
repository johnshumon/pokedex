"""Translation module"""
import json

from app.utils.async_client import client
from app.core.config import settings


async def shakespeare_translation(text: str) -> str:
    """Returns shakespeare translation
    of the given text
    """

    # return for empty no/empty text
    if text is None or text == "":
        return

    translation_url = settings.Config.SHAKESPEARE_TRANSLATION_API
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"text": text})

    translated_res = await client.post(translation_url, headers=headers, data=data)
    translated_json = translated_res.json()

    # return translated text if successful
    # otherwise return original
    # ------------------------------------
    if "success" in translated_json:
        translated_text = translated_json["contents"]["translated"]
    else:
        translated_text = text

    return translated_text
