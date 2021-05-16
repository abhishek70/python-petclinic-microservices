from pydantic import BaseModel


class PetTypeBase(BaseModel):
    name: str


class PetTypeCreate(PetTypeBase):
    pass


class PetTypeUpdate(PetTypeBase):
    pass


class PetTypeInDBBase(PetTypeBase):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


# Properties to return to client
class PetType(PetTypeInDBBase):
    pass


# Properties properties stored in DB
class PetTypeInDB(PetTypeInDBBase):
    pass
