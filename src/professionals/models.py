from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from ..db.database import Base, BaseModel
from ..customers.models import Customer


class Professional(Base, BaseModel):
    __tablename__ = "profesionals"

    customer_id = Column(
        'customer_id', 
        Integer, 
        ForeignKey(Customer.id, ondelete='CASCADE'), 
        nullable=False
    )
    expertise = Column(String(30), nullable=False)
