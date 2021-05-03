from fastapi import APIRouter

from .endpoints import visits, pets, actuators

api_router = APIRouter()
api_router.include_router(actuators.router, prefix="/actuators", tags=["actuators"])
api_router.include_router(visits.router, prefix="/visits", tags=["visits"])
api_router.include_router(pets.router, prefix="/pets", tags=["pets"])
