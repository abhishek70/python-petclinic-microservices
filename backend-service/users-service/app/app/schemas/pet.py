import datetime
from typing import Optional
from pydantic import BaseModel


# Shared properties
class PetBase(BaseModel):
    name: Optional[str] = None
    birth_date: Optional[datetime.date] = None


# Properties to receive on item creation
class PetCreate(PetBase):
    name: str
    birth_date: datetime.date


# Properties to receive on item update
class PetUpdate(PetBase):
    pass


# Properties shared by models stored in DB
class PetInDBBase(PetBase):
    id: int
    name: str
    birth_date: datetime.date
    type_id: int
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Pet(PetInDBBase):
    pass


# Properties properties stored in DB
class PetInDB(PetInDBBase):
    pass
