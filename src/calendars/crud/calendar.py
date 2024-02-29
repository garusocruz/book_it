from datetime import datetime
from sqlalchemy.orm import Session
from .. import models, schemas


def get_calendar(db: Session, calendar_id: int):
    return db.query(models.Calendar).filter(models.Calendar.id == calendar_id).first()


def get_calendars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Calendar).offset(skip).limit(limit).all()


def create_calendar(db: Session, calendar: schemas.CalendarCreate):
    db_calendar = models.Calendar(
        place_id = calendar.place_id,
        active = calendar.active,
        created_at = calendar.created_at,
        updated_at = calendar.updated_at
    )
    db.add(db_calendar)
    db.commit()
    db.refresh(db_calendar)
    return db_calendar

def delete_calendar(db:Session, calendar_id: int):
    db_calendar = db.query(models.Calendar).filter(models.Calendar.id == calendar_id).first()
    if not db_calendar:
        return None
    db.delete(db_calendar)
    db.commit()
    return db_calendar
