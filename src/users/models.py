from sqlalchemy import Column, String, Boolean

from ..db.database import Base, BaseModel


class User(Base, BaseModel):
    __tablename__ = "users"

    username = Column(String(100), nullable=False, unique=True, index=True)
    email = Column(String(15), nullable=False, unique=True, index=True)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String(100), nullable=False)
