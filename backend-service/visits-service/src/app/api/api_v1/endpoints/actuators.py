from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Get service status", description="API for getting service status")
def health():
    return {"status": "up"}
