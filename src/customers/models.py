from sqlalchemy import Column, Integer, String, ForeignKey

from ..db.database import Base, BaseModel
from ..users.models import User

class Customer(Base, BaseModel):
    __tablename__ = "customers"


    name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    user_id = Column("user_id", Integer, ForeignKey(User.id), nullable=False, on_delete="CASCADE")