from typing import Any
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get(
    "/{id}",
    response_model=schemas.PetType,
    summary="Get pet type",
    description="API for getting a pet type"
)
def read_pet_type(
        id: int = Path(..., title="", gt=0),
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Read pet type
    :return:
    """
    data = crud.pettype.get(db=db, id=id)
    if data is None:
        raise HTTPException(status_code=404, detail="Pet type not found")
    return data


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PetType,
    summary="Create a pet type",
    description="API for creating a pet type with all required information."
)
def create_pet_type(
        payload: schemas.PetTypeCreate,
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Create a pet type
    :return:
    """
    data = crud.pettype.create(db=db, obj_in=payload)
    return data
