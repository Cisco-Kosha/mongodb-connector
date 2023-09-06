import os
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, HttpUrl, validator
from pydantic_settings import BaseSettings
from logging.config import dictConfig
import logging

from pymongo import MongoClient

from app.utils.logging import LogConfig


class Settings(object):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = "mongodb-connector"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    USERNAME: str = os.getenv('MONGO_USERNAME')
    PASSWORD: str = os.getenv('MONGO_PASSWORD')
    DB_HOST: str = os.getenv('DB_HOST')
    GET_MONGO_URI: str

    uri: str = "mongodb+srv://{}:{}@{}/?retryWrites=true&w=majority".format(
        USERNAME, PASSWORD, DB_HOST)
    # Create a new client and connect to the server
    client: MongoClient = None


settings = Settings()

logger = logging.getLogger(settings.PROJECT_NAME)
logger.info("Logging configured")