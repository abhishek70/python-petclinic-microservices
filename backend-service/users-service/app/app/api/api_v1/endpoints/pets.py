from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get(
    "/",
    response_model=List[schemas.Pet],
    summary="Get pets",
    description="Get pets"
)
def read_pets() -> Any:
    pass


@router.post(
    "/",
    response_model=schemas.Pet,
    summary="Create pet",
    description="Create a pet"
)
def create_pet() -> Any:
    pass


@router.put(
    "/{id}",
    response_model=schemas.Pet,
    summary="Update a pet",
    description="Update a pet"
)
def update_pet() -> Any:
    pass


@router.get(
    "/{id}",
    response_model=schemas.Pet,
    summary="Get a pet",
    description="Get a pet"
)
def read_pet() -> Any:
    pass


@router.delete(
    "/{id}",
    response_model=schemas.Pet,
    summary="Delete a pet",
    description="Delete a pet"
)
def delete_pet() -> Any:
    pass
