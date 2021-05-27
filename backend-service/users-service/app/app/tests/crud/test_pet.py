from datetime import datetime

from sqlalchemy.orm import Session

from app import crud
from app.schemas.pet import PetCreate, PetUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.pettype import create_random_pettype
from app.tests.utils.utils import random_lower_string, random_pet_name


def test_create_pet(db: Session) -> None:
    name = random_pet_name()
    now = datetime.now()
    birth_date = now.strftime('%Y-%m-%d')
    pettype = create_random_pettype(db)
    pet_in = PetCreate(name=name, birth_date=birth_date, type_id=pettype.id)
    user = create_random_user(db)
    pet = crud.pet.create_with_owner(db=db, obj_in=pet_in, owner_id=user.id)
    assert pet.name == name
    assert pet.owner_id == user.id


def test_get_pet(db: Session) -> None:
    name = random_pet_name()
    now = datetime.now()
    birth_date = now.strftime('%Y-%m-%d')
    pettype = create_random_pettype(db)
    pet_in = PetCreate(name=name, birth_date=birth_date, type_id=pettype.id)
    user = create_random_user(db)
    pet = crud.pet.create_with_owner(db=db, obj_in=pet_in, owner_id=user.id)
    stored_pet = crud.pet.get(db=db, id=pet.id)
    assert stored_pet
    assert pet.id == stored_pet.id
    assert pet.name == stored_pet.name
    assert pet.owner_id == stored_pet.owner_id


def test_update_item(db: Session) -> None:
    name = random_pet_name()
    now = datetime.now()
    birth_date = now.strftime('%Y-%m-%d')
    pettype = create_random_pettype(db)
    pet_in = PetCreate(name=name, birth_date=birth_date, type_id=pettype.id)
    user = create_random_user(db)
    pet = crud.pet.create_with_owner(db=db, obj_in=pet_in, owner_id=user.id)
    name2 = random_pet_name()
    pet_update = PetUpdate(name=name2)
    pet2 = crud.pet.update(db=db, db_obj=pet, obj_in=pet_update)
    assert pet.id == pet2.id
    assert pet2.name == name2
    assert pet.owner_id == pet2.owner_id


def test_delete_item(db: Session) -> None:
    name = random_pet_name()
    now = datetime.now()
    birth_date = now.strftime('%Y-%m-%d')
    pettype = create_random_pettype(db)
    pet_in = PetCreate(name=name, birth_date=birth_date, type_id=pettype.id)
    user = create_random_user(db)
    pet = crud.pet.create_with_owner(db=db, obj_in=pet_in, owner_id=user.id)
    pet2 = crud.pet.remove(db=db, id=pet.id)
    pet3 = crud.pet.get(db=db, id=pet.id)
    assert pet3 is None
    assert pet2.id == pet.id
    assert pet2.name == name
    assert pet.owner_id == user.id
