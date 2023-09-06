from typing import ClassVar, Dict


class LogConfig(object):
    """Logging configuration to be set for the app"""

    LOGGER_NAME: str = "mongodb-connector"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "INFO"

    # Logging config
    version: ClassVar[int] = 1
    disable_existing_loggers: ClassVar[bool] = False
    formatters: Dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: Dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: Dict = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }
