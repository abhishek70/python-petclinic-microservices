from sqlalchemy import Column, DateTime, Integer, String

from ..db.base_class import Base


class Visit(Base):
    __tablename__ = "visits"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    pet_id = Column(Integer, index=True, nullable=False)
    description = Column(String(255))
    visit_date = Column(DateTime, nullable=False)
