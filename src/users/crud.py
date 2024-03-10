from datetime import datetime
from fastapi import HTTPException
import sqlalchemy
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import models, schemas


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    try:
        db_user = models.User(
            username = user.username,
            email = user.email,
            disabled = user.disabled,
            hashed_password = pwd_context.hash(user.password),
            created_at = user.created_at,
            updated_at = user.updated_at)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except sqlalchemy.exc.IntegrityError as err:
        raise HTTPException(status_code=400, detail=f"Field {err.args[0].split('users.')[-1]}, already exists")


def update_user(db:Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    
    db_user.username = user.username
    db_user.email = user.email
    db_user.disabled = user.disabled
    db_user.updated_at = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
