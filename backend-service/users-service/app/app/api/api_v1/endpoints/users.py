from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from app import crud, schemas, models
from sqlalchemy.orm import Session
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get(
    "/",
    response_model=List[schemas.User],
    summary="Get list of users",
    description="Get list of users. Only active superuser should be able to get user list.",
)
def read_users() -> Any:
    """
    Get list of users.
    Only active superuser should be able to get user list.
    :return:
    """
    pass


@router.get(
    "/{id}",
    response_model=schemas.User,
    summary="Read user",
    description="Read user"
)
def read_user() -> Any:
    """
    Read user by id. Only active superuser can access
    :return:
    """
    pass


@router.get(
    "/me",
    response_model=schemas.User,
    summary="Read current login user",
    description="Read current login user"
)
def read_user_me() -> Any:
    """
    Read current login user
    :return:
    """
    pass


@router.post(
    "/",
    response_model=schemas.User,
    summary="Create a new user",
    description="Create a new user"
)
def create_user() -> Any:
    """
    Create new user called by active superuser.
    :return:
    """
    pass


@router.post(
    "/open",
    response_model=schemas.User,
    summary="Create a new user from front end",
    description="Create a new user from front end"
)
def create_user_open(
        *,
        db: Session = Depends(deps.get_db),
        password: str = Body(...),
        email: str = Body(...),
        first_name: str = Body(...),
        last_name: str = Body(...)
) -> Any:
    """
    Create new user called from front end
    :return:
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Registration current not allowed"
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system"
        )
    user_in = schemas.UserCreate(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    user = crud.user.create(db=db, obj_in=user_in)
    return user


@router.put(
    "/me",
    response_model=schemas.User,
    summary="Update current login user",
    description="Update current login user"
)
def update_user_me() -> Any:
    """
    Update current login user
    :return:
    """
    pass


@router.put(
    "/{id}",
    response_model=schemas.User,
    summary="Update a user",
    description="Update a user"
)
def update_user() -> Any:
    """
    Update user by id. Only active superuser can update
    :return:
    """
    pass
