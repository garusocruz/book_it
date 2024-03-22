from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserBase(BaseModel):
    username: str
    email: str
    disabled: bool = False


class UserCreate(UserBase):
    password: str
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
    

class  User(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
