from typing import List

from sqlalchemy.orm import Session

from ..models.visit import Visit
from ..schemas.visit import VisitCreate, VisitUpdate
from .base import CRUDBase


class CRUDVisit(CRUDBase[Visit, VisitCreate, VisitUpdate]):
    def get_multi_by_pet(
        self, db: Session, *, pet_id: int, skip: int = 0, limit: int = 100
    ) -> List[Visit]:
        return (
            db.query(self.model)
            .filter(Visit.pet_id == pet_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


visit = CRUDVisit(Visit)
