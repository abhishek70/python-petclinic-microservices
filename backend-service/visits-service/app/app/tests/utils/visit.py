from sqlalchemy.orm import Session

from ... import crud, models
from ...main import app
from ...schemas.visit import VisitCreate
from ..utils.utils import random_datetime, random_integer, random_lower_string


def create_random_visit(db: Session) -> models.Visit:
    pet_id = random_integer()
    description = random_lower_string()
    visit_date = random_datetime()
    visit_in = VisitCreate(
        pet_id=pet_id, description=description, visit_date=visit_date
    )
    return crud.visit.create(db=db, obj_in=visit_in)
