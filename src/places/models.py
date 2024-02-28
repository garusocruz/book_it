from sqlalchemy import Boolean, Column, Integer, String

from ..db.database import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    capacity = Column(Integer)
    is_active = Column(Boolean, default=True)
