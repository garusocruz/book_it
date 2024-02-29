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


@app.post("/schedules/", response_model=schemas.Schedule)
def create_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    return crud.create_schedule(db=db, schedule=schedule)


@app.get("/schedules/", response_model=list[schemas.Schedule])
def read_schedules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_schedules(db, skip=skip, limit=limit)
    return users


@app.get("/schedules/{schedule_id}", response_model=schemas.Schedule)
def read_schedule(schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule(db, schedule_id=schedule_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule


@app.put("/schedules/{schedule_id}", response_model=schemas.Schedule)
def update_place(schedule_id: int, schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = crud.update_schedule(db, schedule_id=schedule_id, schedule=schedule)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_schedule

@app.delete("/schedules/{schedule_id}", response_model=schemas.Schedule)
def delete_place(schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.delete_schedule(db, schedule_id=schedule_id)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_schedule