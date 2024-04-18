from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from ... import crud, models, schemas
from ....db.database import engine, get_db
from ....users import schemas as user_schema
from ....users import service as user_service
from ...adapters import users as user_adapter
from fastapi import APIRouter

router = APIRouter(prefix="/v1/customers", tags=["customer"])

models.Base.metadata.create_all(bind=engine)



@router.post("/customers/", response_model=schemas.Customer)
def create_customer(current_user: Annotated[user_schema.UserCreate, Depends(user_service.get_current_active_user)], customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    customer = crud.create_customer(db=db, customer=customer)

    if not customer:
        raise HTTPException(status_code=400, detail="Cant create customer CPF already exists")
    return customer


@router.get("/me/", response_model=schemas.CustomerUser)
def read_customers(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):   
    customer = user_adapter.get_customer_by_user_id(db=db, user_id=current_user.id)

    return customer

@router.get("/customers/", response_model=list[schemas.Customer])
def read_customers(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers


@router.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_customer(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@router.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], customer_id: int, customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.update_customer(db, customer_id=customer_id, customer=customer)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.delete("/customers/{customer_id}", response_model=schemas.Customer)
def delete_customer(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.delete_customer(db, customer_id=customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer