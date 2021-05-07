from sqlalchemy.orm import Session

from ...main import app
from ... import crud, models
from ...schemas.visit import VisitCreate
from ..utils.utils import random_lower_string, random_datetime, random_integer


def create_random_visit(db: Session) -> models.Visit:
    pet_id = random_integer()
    description = random_lower_string()
    visit_date = random_datetime()
    visit_in = VisitCreate(pet_id=pet_id, description=description, visit_date=visit_date)
    return crud.visit.create(db=db, obj_in=visit_in)

