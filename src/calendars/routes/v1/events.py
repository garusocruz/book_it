from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from . import router
from ... import crud, models, schemas
from .... db.database import get_db, engine
from .... users import service as user_service
from .... users import schemas as user_schema

models.Base.metadata.create_all(bind=engine)


# EVENTS
@router.post("/events/", response_model=schemas.Event)
def create_events(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)


@router.get("/events/", response_model=list[schemas.Event])
def read_events(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_events(db, skip=skip, limit=limit, current_user=current_user)
    return users


@router.get("/events/{event_id}", response_model=schemas.Event)
def read_event(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.get("/events/calendar/{calendar_id}", response_model=list[schemas.Event])
def read_event(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], calendar_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event_by_calendar_id(db, calendar_id=calendar_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.delete("/events/{event_id}", response_model=schemas.Availability)
def delete_event(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], event_id: int, db: Session = Depends(get_db)):
    db_event = crud.delete_event(db, event_id=event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event