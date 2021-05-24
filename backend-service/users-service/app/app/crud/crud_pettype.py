from app.crud.base import CRUDBase
from app.schemas.pettype import PetTypeCreate, PetTypeUpdate
from app.models.pettype import PetType
from sqlalchemy.orm import Session
from typing import List


class CRUDPetType(CRUDBase[PetType, PetTypeCreate, PetTypeUpdate]):
    def get_all(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[PetType]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )


pettype = CRUDPetType(PetType)
