from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class EventBase(BaseModel):
    calendar_id: int
    customer_id: int
    start_at: datetime
    finish_at: datetime


class EventCreate(EventBase):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None



class  Event(EventBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
