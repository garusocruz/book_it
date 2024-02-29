from datetime import datetime
from pydantic import BaseModel


class AvailabilityBase(BaseModel):
    calendar_id: int
    schedule_id: int


class AvailabilityCreate(AvailabilityBase):
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None



class  Availability(AvailabilityBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
