from fastapi import APIRouter

from app.api.api_v1.endpoints import actions, ping

api_router = APIRouter()

api_router.include_router(actions.router, prefix="/actions", tags=["findOne"])
api_router.include_router(ping.router, prefix="/ping", tags=["ping"])
