from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class CustomerPic(BaseModel):
    profile_pic: str

    class Config:
        from_attributes = True

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
    professional_id: Optional[int] = None
    profile_pic: Optional[str] = None

    class Config:
        from_attributes = True

class CustomerProfilePic(BaseModel):
    profile_pic: str

    class Config:
        from_attributes = True