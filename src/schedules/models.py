from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from ..db.database import Base, BaseModel
from ..places.models import Place


class Schedule(Base, BaseModel):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True)
    place_id = Column('place_id', Integer, ForeignKey(Place.id), nullable=False)
    week_day = Column('dia_semana', Integer, nullable=False)
    start_at = Column(DateTime, nullable=False)
    finish_at = Column(DateTime, nullable=False)
