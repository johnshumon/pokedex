"""Home handler module"""

from typing import Dict
from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def read_root() -> Dict:
    """Main handler for the home path"""
    return {"message": "Hello Pokemon lover!"}
