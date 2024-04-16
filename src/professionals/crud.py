from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas


def get_professional(db: Session, professional_id: int):
    return db.query(models.Professional).filter(models.Professional.id == professional_id).first()

def get_professional_by_customer_id(db: Session, customer_id: int):
    return db.query(models.Professional).filter(models.Professional.customer_id == customer_id).first()


def get_professionals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Professional).offset(skip).limit(limit).all()


def create_professioanl(db: Session, professional: schemas.ProfessionalCreate):
    db_professional = models.Professional(
        customer_id = professional.customer_id,
        expertise = professional.expertise,
        created_at = professional.created_at,
        updated_at = professional.updated_at)
    db.add(db_professional)
    db.commit()
    db.refresh(db_professional)
    return db_professional

def update_professional(db:Session, professional_id: int, professional: schemas.ProfessionalCreate):
    db_professional = db.query(models.Professional).filter(models.Professional.id == professional_id).first()
    if not db_professional:
        return None
    
    db_professional.expertise = professional.expertise
    db_professional.updated_at = datetime.now()
    db.commit()
    db.refresh(db_professional)
    return db_professional

def delete_professional(db:Session, professional_id: int):
    db_professional = db.query(models.Professional).filter(models.Professional.id == professional_id).first()
    if not db_professional:
        return None
    db.delete(db_professional)
    db.commit()
    return db_professional
