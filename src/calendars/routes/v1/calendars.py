from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from . import router
from ... import crud, models, schemas
from .... db.database import get_db, engine
from .... users import service as user_service
from .... users import schemas as user_schema

models.Base.metadata.create_all(bind=engine)



# CALENDAR
@router.post("/calendars/", response_model=schemas.Calendar)
def create_calendars(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], calendar: schemas.CalendarCreate, db: Session = Depends(get_db)):
    return crud.create_calendar(db=db, calendar=calendar)


@router.get("/calendars/", response_model=list[schemas.Calendar])
def read_calendar(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_calendars(db, skip=skip, limit=limit)
    return users


@router.get("/calendars/{calendar_id}", response_model=schemas.Calendar)
def read_calendar(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], calendar_id: int, db: Session = Depends(get_db)):
    db_calendar = crud.get_calendar(db, calendar_id=calendar_id)
    if db_calendar is None:
        raise HTTPException(status_code=404, detail="Calendar not found")
    return db_calendar


@router.delete("/calendars/{calendar_id}", response_model=schemas.Availability)
def delete_calendar(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], calendar_id: int, db: Session = Depends(get_db)):
    db_calendar = crud.delete_calendar(db, calendar_id=calendar_id)
    if not db_calendar:
        raise HTTPException(status_code=404, detail="Calendar not found")
    return db_calendar
