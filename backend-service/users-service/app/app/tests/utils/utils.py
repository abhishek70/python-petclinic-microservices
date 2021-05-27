import datetime
import random
import string
from app import models, crud, schemas
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from app.core.config import settings
from typing import Dict


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=20))


def random_datetime() -> datetime:
    return datetime.datetime.now()


def random_integer() -> int:
    return random.randint(1, 1000)


def random_pet_type() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=5))


def create_random_pettype(db: Session) -> models.PetType:
    name = random_pet_type()
    pet_type_in = schemas.pettype.PetTypeCreate(
        name=name
    )
    return crud.pettype.create(db=db, obj_in=pet_type_in)


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


def random_pet_name() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=5))
