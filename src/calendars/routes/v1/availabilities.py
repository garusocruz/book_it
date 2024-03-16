from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from . import router
from ... import crud, models, schemas
from .... db.database import get_db, engine
from .... users import service as user_service
from .... users import schemas as user_schema

models.Base.metadata.create_all(bind=engine)


# AVAILABILITIES
@router.post("/availabilities/", response_model=schemas.Availability)
def create_availabilities(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], availability: schemas.AvailabilityCreate, db: Session = Depends(get_db)):
    return crud.create_availability(db=db, availability=availability)


@router.get("/availabilities/", response_model=list[schemas.Availability])
def readavailabilities(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_availabilities(db, skip=skip, limit=limit)
    return users


@router.get("/availabilities/{availability_id}", response_model=schemas.Availability)
def read_availabilities(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], availability_id: int, db: Session = Depends(get_db)):
    db_availability = crud.get_availability(db, availability_id=availability_id)
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    return db_availability


@router.delete("/availabilities/{availability_id}", response_model=schemas.Availability)
def delete_availabilities(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], availability_id: int, db: Session = Depends(get_db)):
    db_availability = crud.delete_availability(db, availability_id=availability_id)
    if not db_availability:
        raise HTTPException(status_code=404, detail="Availability not found")
    return db_availability
