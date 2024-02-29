from datetime import datetime
import sqlite3
import sqlalchemy
from sqlalchemy.orm import Session
from . import models, schemas


def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: schemas.CustomerCreate):
    try:
        db_customer = models.Customer(
            name = customer.name,
            phone = customer.phone,
            cpf = customer.cpf,
            created_at = customer.created_at,
            updated_at = customer.updated_at)
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    except sqlalchemy.exc.IntegrityError:
        return None

def update_customer(db:Session, customer_id: int, customer: schemas.CustomerCreate):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        return None
    
    db_customer.name = customer.name
    db_customer.phone = customer.phone
    db_customer.cpf = customer.cpf
    db_customer.updated_at = datetime.now()
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db:Session, customer_id: int):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        return None
    db.delete(db_customer)
    db.commit()
    return db_customer
