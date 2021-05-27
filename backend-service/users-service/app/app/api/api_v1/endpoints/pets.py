from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.api import deps

router = APIRouter()


@router.get(
    "/",
    response_model=List[schemas.Pet],
    summary="Get pets",
    description="Get pets for current active user"
)
def read_pets(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get all pets for the active user
    :param db:
    :param skip:
    :param limit:
    :param current_user:
    :return:
    """
    if crud.user.is_superuser(current_user):
        return crud.pet.get_multi(db=db, skip=skip, limit=limit)
    else:
        return crud.pet.get_multi_by_owner(db=db, owner_id=current_user.id, skip=skip, limit=limit)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Pet,
    summary="Create pet",
    description="Create pet for the current active user"
)
def create_pet(
        *,
        db: Session = Depends(deps.get_db),
        pet_in: schemas.PetCreate,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create pet for the current active user
    :param db:
    :param pet_in:
    :param current_user:
    :return:
    """
    return crud.pet.create_with_owner(db=db, obj_in=pet_in, owner_id=current_user.id)


@router.put(
    "/{id}",
    response_model=schemas.Pet,
    summary="Update pet by id",
    description="Update pet for current active user"
)
def update_pet(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        pet_in: schemas.PetUpdate,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update pet for current active user
    :param db:
    :param id:
    :param pet_in:
    :param current_user:
    :return:
    """
    pet = crud.pet.get(db=db, id=id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    if not crud.user.is_superuser(current_user) and (pet.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return crud.pet.update(db=db, db_obj=pet, obj_in=pet_in)


@router.get(
    "/{id}",
    response_model=schemas.Pet,
    summary="Get pet by id",
    description="Get pet for current active user"
)
def read_pet(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get pet by id
    :param db:
    :param id:
    :param current_user:
    :return:
    """
    pet = crud.pet.get(db=db, id=id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    if not crud.user.is_superuser(current_user) and (pet.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return pet


@router.delete(
    "/{id}",
    response_model=schemas.Pet,
    summary="Delete pet by id",
    description="Delete pet for current active user"
)
def delete_pet(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete pet by id
    :param db:
    :param id:
    :param current_user:
    :return:
    """
    pet = crud.pet.get(db=db, id=id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    if not crud.user.is_superuser(current_user) and (pet.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return crud.pet.remove(db=db, id=id)
