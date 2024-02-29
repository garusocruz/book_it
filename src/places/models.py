from sqlalchemy import Boolean, Column, Integer, String, ForeignKey

from ..db.database import Base, BaseModel
from ..customers.models import Customer

from ..db.database import Base, BaseModel
class Place(Base, BaseModel):
    __tablename__ = "places"

    owner_id = Column("owner_id",Integer, ForeignKey(Customer.id))
    name = Column(String(100))
    description = Column(String(255))
    capacity = Column(Integer)
    is_active = Column(Boolean, default=True)
