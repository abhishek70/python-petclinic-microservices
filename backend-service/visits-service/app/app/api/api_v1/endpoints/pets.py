from typing import Any, List

from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.orm import Session

from .... import crud, schemas
from ... import deps

router = APIRouter()


@router.get(
    "/{id}/visits",
    response_model=List[schemas.Visit],
    status_code=status.HTTP_200_OK,
    summary="Get pet visits",
    description="API for getting all pet visit details.",
)
def read_visit(
    id: int = Path(..., title="", gt=0),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get pet visits
    :param limit:
    :param skip:
    :param id:
    :param db:
    :return:
    """
    return crud.visit.get_multi_by_pet(db=db, pet_id=id, skip=skip, limit=limit)
