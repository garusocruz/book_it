from sqlalchemy import Column, String, ForeignKey, Integer

from src.places.models import Place

from ..db.database import Base, BaseModel

class Schedule(Base, BaseModel):
    __tablename__ = "schedules"
    place_id = Column('place_id', Integer, ForeignKey(Place.id), nullable=False)
    week_day = Column('week_day', Integer, nullable=False) # 0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday
    start_at = Column(String, nullable=False)
    finish_at = Column(String, nullable=False)
