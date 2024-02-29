from datetime import datetime
from pydantic import BaseModel



class ScheduleBase(BaseModel):
    place_id: int
    week_day: int
    start_at: datetime
    finish_at: datetime


class ScheduleCreate(ScheduleBase):
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None
    

class  Schedule(ScheduleBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
