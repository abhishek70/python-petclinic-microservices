from sqlalchemy.orm import Session

from ...main import app
from ... import crud
from ...schemas.visit import VisitCreate, VisitUpdate
from ..utils.utils import random_lower_string, random_datetime, random_integer


def test_create_visit(db: Session) -> None:
    pet_id = random_integer()
    description = random_lower_string()
    visit_date = random_datetime()
    visit_in = VisitCreate(pet_id=pet_id, description=description, visit_date=visit_date)
    visit = crud.visit.create(db=db, obj_in=visit_in)
    assert visit.pet_id == pet_id
    assert visit.description == description
    assert visit.visit_date == visit_date


def test_get_visit(db: Session) -> None:
    pet_id = random_integer()
    description = random_lower_string()
    visit_date = random_datetime()
    visit_in = VisitCreate(pet_id=pet_id, description=description, visit_date=visit_date)
    visit = crud.visit.create(db=db, obj_in=visit_in)
    store_db_visit = crud.visit.get(db=db, id=visit.id)
    assert store_db_visit
    assert store_db_visit.pet_id == pet_id
    assert store_db_visit.visit_date == visit_date


def test_update_visit(db: Session) -> None:
    pet_id = random_integer()
    description = random_lower_string()
    visit_date = random_datetime()
    visit_in = VisitCreate(pet_id=pet_id, description=description, visit_date=visit_date)
    visit = crud.visit.create(db=db, obj_in=visit_in)
    description2 = random_lower_string()
    visit_date2 = random_datetime()
    visit_update = VisitUpdate(description=description2, visit_date=visit_date2)
    visit2 = crud.visit.update(db=db, db_obj=visit, obj_in=visit_update)
    store_db_visit = crud.visit.get(db=db, id=visit.id)
    assert store_db_visit
    assert store_db_visit.description == description2
    assert store_db_visit.visit_date == visit_date2


def test_delete_visit(db: Session) -> None:
    pet_id = random_integer()
    description = random_lower_string()
    visit_date = random_datetime()
    visit_in = VisitCreate(pet_id=pet_id, description=description, visit_date=visit_date)
    visit = crud.visit.create(db=db, obj_in=visit_in)
    delete_visit = crud.visit.remove(db=db, id=visit.id)
    get_visit = crud.visit.get(db=db, id=visit.id)
    assert delete_visit.pet_id == pet_id
    assert delete_visit.visit_date == visit_date
    assert get_visit is None


def test_get_multi_by_pet(db: Session) -> None:
    pet_id = random_integer()
    description = random_lower_string()
    visit_date = random_datetime()
    visit_in = VisitCreate(pet_id=pet_id, description=description, visit_date=visit_date)
    visit = crud.visit.create(db=db, obj_in=visit_in)
    description2 = random_lower_string()
    visit_date2 = random_datetime()
    visit_in2 = VisitCreate(pet_id=pet_id, description=description2, visit_date=visit_date2)
    visit2 = crud.visit.create(db=db, obj_in=visit_in2)
    get_visits = crud.visit.get_multi_by_pet(db=db, pet_id=pet_id, skip=0, limit=2)
    assert len(get_visits) == 2
