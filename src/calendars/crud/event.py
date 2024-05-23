from datetime import datetime
from sqlalchemy.orm import Session
from .. import models, schemas


def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def get_event_by_calendar_id(db: Session, calendar_id: int):
    return db.query(models.Event).filter(models.Event.calendar_id == calendar_id).all()

def get_events(db: Session, skip: int = 0, limit: int = 100, ):
    return db.query(models.Event).offset(skip).limit(limit).all()


def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(
        calendar_id = event.calendar_id,
        customer_id = event.customer_id,
        start_at = event.start_at,
        finish_at = event.finish_at,
        created_at = event.created_at,
        updated_at = event.updated_at
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db:Session, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not db_event:
        return None
    db.delete(db_event)
    db.commit()
    return db_event
