from sqlalchemy import Column, Integer, String

from ..db.database import Base, BaseModel


class Customer(Base, BaseModel):
    __tablename__ = "customers"

    name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    