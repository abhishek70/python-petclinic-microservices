from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from ... import deps
from .... import crud, schemas

router = APIRouter()


@router.get(
    "/{id}",
    response_model=schemas.Visit,
    status_code=status.HTTP_200_OK,
    summary="Get visit",
    description="API for getting a visit details."
)
def read_visit(
        id: int = Path(..., title="", gt=0),
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get visit
    :param id:
    :param db:
    :return:
    """
    data = crud.visit.get(db=db, id=id)
    if data is None:
        raise HTTPException(status_code=404, detail="Visit not found")
    return data


@router.post(
    "/",
    response_model=schemas.Visit,
    status_code=status.HTTP_201_CREATED,
    summary="Create visit",
    description="API for creating a visit with all required information."
)
def create_visit(
        payload: schemas.VisitCreate,
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Create visit
    :param payload:
    :param db:
    :return:
    """
    data = crud.visit.create(db=db, obj_in=payload)
    return data


@router.put(
    "/{id}",
    response_model=schemas.Visit,
    status_code=status.HTTP_200_OK,
    summary="Update visit",
    description="API for updating a visit with all required information."
)
def update_visit(
        payload: schemas.VisitUpdate,
        id: int = Path(..., title="", gt=0),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update visit
    :param id:
    :param payload:
    :param db:
    :return:
    """
    data = crud.visit.get(db=db, id=id)
    if data is None:
        raise HTTPException(status_code=404, detail="Visit not found")
    data = crud.visit.update(db=db, db_obj=data, obj_in=payload)
    return data


@router.delete(
    "/{id}",
    response_model=schemas.Visit,
    status_code=status.HTTP_200_OK,
    summary="Delete visit",
    description="API for deleting a visit"
)
def delete_visit(
        id: int = Path(..., title="", gt=0),
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete visit
    :param id:
    :param db:
    :return:
    """
    data = crud.visit.get(db=db, id=id)
    if data is None:
        raise HTTPException(status_code=404, detail="Visit not found")
    data = crud.visit.remove(db=db, id=id)
    return data
