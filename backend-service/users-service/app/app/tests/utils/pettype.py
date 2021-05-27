from sqlalchemy.orm import Session
from app import crud
from app.models.pettype import PetType
from app.schemas.pettype import PetTypeCreate
from app.tests.utils.utils import random_pet_type


def create_random_pettype(db: Session) -> PetType:
    name = random_pet_type()
    pettype_in = PetTypeCreate(name=name)
    return crud.pettype.create(db=db, obj_in=pettype_in)
