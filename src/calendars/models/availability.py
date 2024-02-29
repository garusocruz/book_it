from sqlalchemy import Boolean, Column, ForeignKey, Integer

from ...db.database import Base, BaseModel
from ...schedules.models import Schedule
from ...calendars.models.calendar import Calendar



class Availability(Base, BaseModel):
    __tablename__ = "availabilities"

    calendar_id = Column("calendar_id", Integer, ForeignKey(Calendar.id), nullable=False)
    schedule_id = Column("schedule_id", Integer, ForeignKey(Schedule.id), nullable=False)
    