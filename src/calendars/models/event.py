from sqlalchemy import Boolean, Column, ForeignKey, Integer

from ...db.database import Base, BaseModel
from ...customers.models import Customer
from ...schedules.models import Schedule
from ...calendars.models.calendar import Calendar
    

class Event(Base, BaseModel):
    __tablename__ = "events"

    calendar_id = Column("calendar_id", Integer, ForeignKey(Calendar.id), nullable=False, on_delete="CASCADE")
    customer_id = Column("customer_id", Integer, ForeignKey(Customer.id), nullable=False, on_delete="CASCADE")
    schedule_id = Column("schedule_id", Integer, ForeignKey(Schedule.id), nullable=False, on_delete="CASCADE")