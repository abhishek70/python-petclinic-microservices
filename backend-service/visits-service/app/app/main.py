from fastapi import FastAPI

from .api.api_v1.api import api_router
from .core.config import settings

# from .db.init_db import init_db
# from .db.session import SessionLocal
#
# db = SessionLocal()
# init_db(db)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url=f"{settings.API_V1_STR}/docs",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(api_router, prefix=settings.API_V1_STR)
