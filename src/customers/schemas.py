from datetime import datetime
from pydantic import BaseModel
from typing import Optional



class CustomerBase(BaseModel):
    name: str
    phone: str
    cpf: str
    user_id: int


class CustomerCreate(CustomerBase):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
    

class  Customer(CustomerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CustomerUser(Customer):
    user_id: int
    email: str
    username: str
    created_at: datetime

    class Config:
        from_attributes = True
