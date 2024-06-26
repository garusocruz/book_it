from datetime import datetime
from sqlalchemy.orm import Session

from . import models, schemas
from ..users import schemas as user_schema


def get_place(db: Session, place_id: int):
    return db.query(models.Place).filter(models.Place.id == place_id).first()

def get_place_by_professional_id(db: Session, professional_id: int):
    return db.query(models.Place).filter(models.Place.owner_id == professional_id)


def get_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Place).offset(skip).limit(limit).all()


def create_place(db: Session, place: schemas.PlaceCreate, current_user: user_schema.User):
    db_place = models.Place(
        name = place.name, 
        description = place.description,
        capacity = place.capacity,
        is_active = place.is_active,
        created_at = datetime.now(),
        owner_id = current_user.id)
    
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

def update_place(db:Session, place_id: int, place: schemas.PlaceCreate):
    db_place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not db_place:
        return None
    db_place.name = place.name
    db_place.description = place.description
    db_place.capacity = place.capacity
    db_place.is_active = place.is_active
    db.commit()
    db.refresh(db_place)
    return db_place

def delete_place(db:Session, place_id: int):
    db_place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not db_place:
        return None
    db.delete(db_place)
    db.commit()
    return db_place
