from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

if TYPE_CHECKING:
    from .pet import Pet  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    first_name = Column(String(20), index=True, nullable=False)
    last_name = Column(String(20), index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    pets = relationship("Pet", back_populates="owner")
