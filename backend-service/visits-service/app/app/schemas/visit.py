from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


# Shared properties
class VisitBase(BaseModel):
    # pet_id: int = Field(0, gt=0)
    description: Optional[str] = Field(
        None, title="The description of the visit", max_length=255
    )
    visit_date: datetime


# Properties to receive on visit creation
class VisitCreate(VisitBase):
    pet_id: int = Field(0, gt=0)
    visit_date: datetime


# Properties to receive on item update
class VisitUpdate(VisitBase):
    # description: Optional[str] = Field(None, title="The description of the visit", max_length=255)
    # visit_date: datetime
    pass


# Properties shared by models stored in DB
class VisitInDBBase(VisitBase):
    id: int
    pet_id: int
    visit_date: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


# Properties to return to client
class Visit(VisitInDBBase):
    pass


# Properties properties stored in DB
class VisitInDB(VisitInDBBase):
    pass
