from datetime import datetime
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    username: str
    email: str
    disabled: bool | None = None


class UserCreate(UserBase):
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime | None = None
    

class  User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
