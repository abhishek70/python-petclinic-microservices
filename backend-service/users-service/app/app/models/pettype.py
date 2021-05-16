from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

if TYPE_CHECKING:
    from .pet import Pet  # noqa: F401


class PetType(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String(20), index=True, nullable=False)
    pettypes = relationship("Pet", back_populates="type")
