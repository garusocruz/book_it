from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from ..db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# AVAILABILITIES
@app.post("/availabilities/", response_model=schemas.Availability)
def create_availabilities(availability: schemas.AvailabilityCreate, db: Session = Depends(get_db)):
    return crud.create_availability(db=db, availability=availability)


@app.get("/availabilities/", response_model=list[schemas.Availability])
def readavailabilities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_availabilities(db, skip=skip, limit=limit)
    return users


@app.get("/availabilities/{availability_id}", response_model=schemas.Availability)
def read_availabilities(availability_id: int, db: Session = Depends(get_db)):
    db_availability = crud.get_availability(db, availability_id=availability_id)
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    return db_availability


@app.delete("/availabilities/{availability_id}", response_model=schemas.Availability)
def delete_availabilities(availability_id: int, db: Session = Depends(get_db)):
    db_availability = crud.delete_availability(db, availability_id=availability_id)
    if not db_availability:
        raise HTTPException(status_code=404, detail="Availability not found")
    return db_availability

# CALENDAR
@app.post("/calendars/", response_model=schemas.Calendar)
def create_calendars(calendar: schemas.CalendarCreate, db: Session = Depends(get_db)):
    return crud.create_calendar(db=db, calendar=calendar)


@app.get("/calendars/", response_model=list[schemas.Calendar])
def read_calendar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_calendars(db, skip=skip, limit=limit)
    return users


@app.get("/calendars/{calendar_id}", response_model=schemas.Calendar)
def read_calendar(calendar_id: int, db: Session = Depends(get_db)):
    db_calendar = crud.get_calendar(db, calendar_id=calendar_id)
    if db_calendar is None:
        raise HTTPException(status_code=404, detail="Calendar not found")
    return db_calendar


@app.delete("/calendars/{calendar_id}", response_model=schemas.Availability)
def delete_calendar(calendar_id: int, db: Session = Depends(get_db)):
    db_calendar = crud.delete_calendar(db, calendar_id=calendar_id)
    if not db_calendar:
        raise HTTPException(status_code=404, detail="Calendar not found")
    return db_calendar
