import datetime
import random
import string
from app import models, crud, schemas
from sqlalchemy.orm import Session


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


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
