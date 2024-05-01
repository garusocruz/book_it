from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from ....users import service as user_service
from ....users import schemas as user_schema


from ... import crud, models, schemas
from ....db.database import engine, get_db
from fastapi import APIRouter, Response, status
models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/v1/schedules", tags=["schedule"])


@router.post("/", response_model=schemas.Schedule)
def create_schedule(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    return crud.create_schedule(db=db, schedule=schedule)


@router.get("/", response_model=list[schemas.Schedule])
def read_schedules(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_schedules(db, skip=skip, limit=limit)
    return users


@router.get("/{schedule_id}", response_model=schemas.Schedule)
def read_schedule(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule(db, schedule_id=schedule_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule

@router.get("/place/{place_id}", response_model=list[schemas.Schedule])
def read_schedule(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], place_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule_by_place_id(db, place_id=place_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule


@router.put("/{schedule_id}", response_model=schemas.Schedule)
def update_place(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], schedule_id: int, schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = crud.update_schedule(db, schedule_id=schedule_id, schedule=schedule)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_schedule

@router.delete("/{schedule_id}", response_model=schemas.Schedule)
def delete_place(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.delete_schedule(db, schedule_id=schedule_id)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_schedule