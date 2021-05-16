from app.crud.base import CRUDBase
from app.schemas.pettype import PetTypeCreate, PetTypeUpdate
from app.models.pettype import PetType


class CRUDPetType(CRUDBase[PetType, PetTypeCreate, PetTypeUpdate]):
    pass


pettype = CRUDPetType(PetType)
