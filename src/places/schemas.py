from pydantic import BaseModel
from typing import Optional


class PlaceBase(BaseModel):
    capacity: int
    description: Optional[str] = None
    is_active: bool
    name: str
    


class PlaceCreate(PlaceBase):
    pass


class  Place(PlaceBase):
    id: int

    class Config:
        from_attributes = True
