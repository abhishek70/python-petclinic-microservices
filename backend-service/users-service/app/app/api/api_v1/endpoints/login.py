from typing import Any
from datetime import timedelta

from app.core.security import get_password_hash
from app.utils import generate_password_reset_token, send_reset_password_email, verify_password_reset_token
from fastapi import APIRouter, HTTPException, Depends, Body
from app import crud, schemas, models
from app.api import deps
from app.core import security
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.config import settings

router = APIRouter()


@router.post(
    "/access-token",
    response_model=schemas.Token,
    summary="Get access token",
    description="OAuth2 compatible token login, get an access token for future requests"
)
def login_access_token(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    :param db:
    :param form_data:
    :return:
    """
    user = crud.user.authenticate(
        db=db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    token_expiry = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=token_expiry
        ),
        "token_type": "bearer",
    }


@router.post("/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user


@router.post(
    "/password-recovery/{email}",
    response_model=schemas.Msg,
    summary="Password recovery",
    description="Password recovery"
)
def recover_password(
    email: str,
        db: Session = Depends(deps.get_db)
) -> Any:
    """
    Password recovery
    :return:
    """
    user = crud.user.get_by_email(db, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}


@router.post(
    "/reset-password/",
    response_model=schemas.Msg,
    summary="Reset password",
    description="Reset password"
)
def reset_password(
        token: str = Body(...),
        new_password: str = Body(...),
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Reset password
    :return:
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully"}
