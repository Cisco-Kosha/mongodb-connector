from typing import List, Any

from fastapi import APIRouter, HTTPException
from pymongo.mongo_client import MongoClient

from app.core.config import settings, logger

# Send a ping to confirm a successful connection

router = APIRouter()

client = MongoClient(settings.uri)


@router.get("/", response_model=Any)
def ping() -> Any:
    try:
        resp = client.admin.command('ping')
        return resp
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
