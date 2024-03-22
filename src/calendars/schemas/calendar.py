from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class CalendarBase(BaseModel):
    place_id: int
    active: bool

class CalendarCreate(CalendarBase):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None



class  Calendar(CalendarBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
