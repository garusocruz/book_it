from datetime import datetime
from pydantic import BaseModel



class CustomerBase(BaseModel):
    name: str
    phone: str
    cpf: str
    user_id: int


class CustomerCreate(CustomerBase):
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None
    

class  Customer(CustomerBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
