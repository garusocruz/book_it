from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas 
from ..users import schemas as user_schema


def get_schedule(db: Session, schedule_id: int):
    return db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()

def get_schedule_by_place_id(db: Session, place_id: int):
    return db.query(models.Schedule).filter(models.Schedule.place_id == place_id)


def get_schedules(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Schedule).offset(skip).limit(limit).all()


def create_schedule(db: Session, schedule: schemas.ScheduleCreate):
    db_schedule = models.Schedule(
        place_id = schedule.place_id,
        week_day = schedule.week_day,
        start_at = schedule.start_at,
        finish_at = schedule.finish_at,
        created_at = schedule.created_at,
        updated_at = schedule.updated_at)
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def update_schedule(db:Session, schedule_id: int, schedule: schemas.ScheduleCreate):
    db_schedule = db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()
    if not db_schedule:
        return None
    
    db_schedule.place_id = schedule.place_id
    db_schedule.week_day = schedule.week_day
    db_schedule.updated_at = datetime.now()
    db_schedule.start_at = schedule.start_at
    db_schedule.finish_at = schedule.finish_at
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def delete_schedule(db:Session, schedule_id: int):
    db_schedule = db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()
    if not db_schedule:
        return None
    db.delete(db_schedule)
    db.commit()
    return db_schedule
