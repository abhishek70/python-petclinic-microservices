from sqlalchemy.orm import Session

from app import crud
from app.schemas.pettype import PetTypeCreate
from app.tests.utils.utils import random_integer, random_pet_type


def test_create_pettype(db: Session) -> None:
    name = random_pet_type()
    pet_type_in = PetTypeCreate(
        name=name
    )
    pet_type = crud.pettype.create(db=db, obj_in=pet_type_in)
    assert pet_type.name == name


def test_get_pettype(db: Session) -> None:
    name = random_pet_type()
    pet_type_in = PetTypeCreate(
        name=name
    )
    pet_type = crud.pettype.create(db=db, obj_in=pet_type_in)
    store_db_pet_type = crud.pettype.get(db=db, id=pet_type.id)
    assert store_db_pet_type
    assert store_db_pet_type.name == name
