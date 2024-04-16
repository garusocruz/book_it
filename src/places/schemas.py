from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PlaceBase(BaseModel):
    capacity: int
    description: Optional[str] = None
    is_active: bool
    name: str
    owner_id: int
    


class PlaceCreate(PlaceBase):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None


class  Place(PlaceBase):
    id: int

    class Config:
        from_attributes = True
