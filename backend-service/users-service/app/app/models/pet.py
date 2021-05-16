from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .pettype import PetType  # noqa: F401


class Pet(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String(20), index=True, nullable=False)
    birth_date = Column(Date, index=True, nullable=False)
    type_id = Column(Integer, ForeignKey("pettype.id"))
    type = relationship("PetType", back_populates="pettypes")
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="pets")
