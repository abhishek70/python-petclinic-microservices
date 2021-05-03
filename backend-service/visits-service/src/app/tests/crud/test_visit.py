from sqlalchemy.orm import Session

from ...main import app
from ... import crud
from ...schemas.visit import VisitCreate, VisitUpdate


def test_create_visit(db: Session) -> None:
    pet_id = 1
    description = "Test visit"
    visit_date = "2021-05-03 04:37:36.861000"
    visit_in = VisitCreate(pet_id=pet_id, description=description, visit_date=visit_date)
    visit = crud.visit.create(db=db, obj_in=visit_in)
    assert visit.pet_id == pet_id
    assert visit.description == description
