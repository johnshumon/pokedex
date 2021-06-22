"""Application server module"""

import uvicorn

from fastapi import FastAPI

from app.core import settings
from app.apis.v1 import api_router

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix=settings.API_V1_STR)

PORT = int(settings.Config.PORT) or 9000


def init_server() -> None:
    uvicorn.run("app.server:app", host="0.0.0.0", port=PORT, reload=True)
