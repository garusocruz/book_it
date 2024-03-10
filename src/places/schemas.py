from pydantic import BaseModel


class PlaceBase(BaseModel):
    capacity: int
    description: str | None = None
    is_active: bool
    name: str
    


class PlaceCreate(PlaceBase):
    pass


class  Place(PlaceBase):
    id: int

    class Config:
        from_attributes = True
