from datetime import datetime
from sqlalchemy.orm import Session
from .. import models, schemas


def get_availability(db: Session, availability_id: int):
    return db.query(models.Availability).filter(models.Availability.id == availability_id).first()


def get_availabilities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Availability).offset(skip).limit(limit).all()


def create_availability(db: Session, availability: schemas.AvailabilityCreate):
    db_availability = models.Availability(
        calendar_id = availability.calendar_id,
        schedule_id = availability.schedule_id,
        created_at = availability.created_at,
        updated_at = availability.updated_at
    )
    db.add(db_availability)
    db.commit()
    db.refresh(db_availability)
    return db_availability

def delete_availability(db:Session, availability_id: int):
    db_availability = db.query(models.Availability).filter(models.Availability.id == availability_id).first()
    if not db_availability:
        return None
    db.delete(db_availability)
    db.commit()
    return db_availability
