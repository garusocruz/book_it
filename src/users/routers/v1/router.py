from datetime import datetime, timedelta, timezone
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from typing import Annotated
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from sqlalchemy.orm import Session
from ... import service as user_service

from ... import crud, models, schemas
from ....db.database import engine, get_db
from fastapi import APIRouter, Response, status
models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/v1/users", tags=["user"])


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    import ipdb
    ipdb.set_trace()
    user = crud.create_user(db=db, user=user)

    if not user:
        raise HTTPException(status_code=400, detail="Cant create user Username already exists")
    return user


@router.get("/", response_model=list[schemas.User])
def users(current_user: Annotated[schemas.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(current_user: Annotated[schemas.User, Depends(user_service.get_current_active_user)], user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(current_user: Annotated[schemas.User, Depends(user_service.get_current_active_user)], user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id=user_id, user=user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(current_user: Annotated[schemas.User, Depends(user_service.get_current_active_user)], user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user