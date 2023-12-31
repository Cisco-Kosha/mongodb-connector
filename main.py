
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings, logger
from app.api.api_v1.api import api_router
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"/openapi.json",
    docs_url="/docs"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Starting mongodb-connector app")
logger.info("Exposing /metrics endpoint for metrics scrapping")

Instrumentator().instrument(app).expose(app)

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Hello World"}