from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from app import crud, schemas, models
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()


@router.get(
    "/",
    response_model=List[schemas.User],
    summary="Get list of users",
    description="Get list of users. Only active superuser should be able to get user list.",
)
def read_users(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Get list of users.
    Only active superuser should be able to get user list.
    :return:
    """
    return crud.user.get_multi(db=db, skip=skip, limit=limit)


@router.get(
    "/me",
    response_model=schemas.User,
    summary="Read current login user",
    description="Read current login user"
)
def read_user_me(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Read current login user
    :return:
    """
    return current_user


@router.put(
    "/me",
    response_model=schemas.User,
    summary="Update current login user",
    description="Update current login user"
)
def update_user_me(
        *,
        db: Session = Depends(deps.get_db),
        password: str = Body(None),
        first_name: str = Body(None),
        last_name: str = Body(None),
        email: EmailStr = Body(None),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update current login user
    :return:
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if first_name is not None:
        user_in.first_name = first_name
    if last_name is not None:
        user_in.last_name = last_name
    if email is not None:
        user_in.email = email
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get(
    "/{id}",
    response_model=schemas.User,
    summary="Read user by id",
    description="Read user by id"
)
def read_user_by_id(
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Read user by id. Only active superuser can access.
    :return:
    """
    user = crud.user.get(db, id=id)
    if user == current_user:
        return user
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    elif not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.User,
    summary="Create new user",
    description="Create a new user"
)
def create_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.UserCreate,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Only active superuser should be able to create a new user.
    :return:
    """
    user = crud.user.get_by_email(db=db, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="The user with this username already exists in the system.")
    user = crud.user.create(db=db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
    return user


@router.post(
    "/open",
    status_code=status.HTTP_201_CREATED,
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
    "/{id}",
    response_model=schemas.User,
    summary="Update a user",
    description="Update a user"
)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update user by id. Only active superuser can update
    :return:
    """
    user = crud.user.get(db, id=id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user
