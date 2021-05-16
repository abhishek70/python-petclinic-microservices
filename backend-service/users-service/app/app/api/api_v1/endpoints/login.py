from typing import Any
from fastapi import APIRouter, HTTPException, Depends
from app import crud, schemas, models

router = APIRouter()

@router.post(
    "/access-token",
    response_model=schemas.Token
)
def login_access_token() -> Any:
    """
    :param db:
    :param form_data:
    :return:
    """
    pass

@router.post(
    "/password-recovery/{email}",
    response_model=schemas.Msg
)
def recover_password() -> Any:
    """
    Password recovery
    :return:
    """
    pass

@router.post(
    "/reset-password/",
    response_model=schemas.Msg
)
def reset_password() -> Any:
    """
    Reset password
    :return:
    """
    pass