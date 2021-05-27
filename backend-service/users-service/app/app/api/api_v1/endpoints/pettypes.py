from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get(
    "/",
    response_model=List[schemas.PetType],
    summary="Get pet types",
    description="API for getting all pet types"
)
def read_pet_types(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Read pet types
    :return:
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud.pettype.get_all(db=db, skip=skip, limit=limit)


@router.get(
    "/{id}",
    response_model=schemas.PetType,
    summary="Get pet type by id",
    description="API for getting a pet type"
)
def read_pet_type(
        id: int = Path(..., title="", gt=0),
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Read pet type by id
    :return:
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=403, detail="Not enough permissions")
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
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Create a pet type
    :return:
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud.pettype.create(db=db, obj_in=payload)
