from sqlalchemy import Boolean, Column, ForeignKey, Integer

from ...db.database import Base, BaseModel
from ...places.models import Place


class Calendar(Base, BaseModel):
    __tablename__ = "calendars"

    place_id = Column('place_id', Integer, ForeignKey(Place.id), nullable=False)
    active = Column(Boolean, default=False)