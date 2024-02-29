from datetime import datetime
from pydantic import BaseModel


class EventBase(BaseModel):
    calendar_id: int
    schedule_id: int
    customer_id: int


class EventCreate(EventBase):
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None



class  Event(EventBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
