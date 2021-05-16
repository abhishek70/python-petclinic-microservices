from fastapi import APIRouter

from app.api.api_v1.endpoints import actuators, users, login, pettypes, pets

api_router = APIRouter()
api_router.include_router(actuators.router, tags=["actuators"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(pets.router, prefix="/pets", tags=["pets"])
api_router.include_router(pettypes.router, prefix="/pettypes", tags=["pettypes"])
