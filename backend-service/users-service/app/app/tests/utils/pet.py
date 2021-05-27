from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session

from app import crud, models
from app.tests.utils.user import create_random_user
from app.schemas.pet import PetCreate
from .pettype import create_random_pettype
from app.tests.utils.utils import random_pet_name


def create_random_pet(db: Session, owner_id: Optional[int] = None) -> models.Pet:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    name = random_pet_name()
    now = datetime.now()
    birth_date = now.strftime('%Y-%m-%d')
    pet_type = create_random_pettype(db)
    pet_in = PetCreate(name=name, birth_date=birth_date, type_id=pet_type.id)
    return crud.pet.create_with_owner(db=db, obj_in=pet_in, owner_id=owner_id)
