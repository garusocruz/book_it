from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class AvailabilityBase(BaseModel):
    calendar_id: int
    schedule_id: int


class AvailabilityCreate(AvailabilityBase):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None



class  Availability(AvailabilityBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
