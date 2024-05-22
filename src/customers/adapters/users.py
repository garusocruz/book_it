from sqlalchemy import or_
from sqlalchemy.orm import Session
from ...customers import models as customer_models, schemas as customer_schemas
from ...users import crud as user_crud
from ...professionals import crud as professional_crud

def get_customer_by_user_id(db: Session, user_id: int):
    customer_data = db.query(customer_models.Customer).filter(customer_models.Customer.user_id == user_id).first()
    user_data = user_crud.get_user(db=db, user_id=user_id)
    professional_data = professional_crud.get_professional_by_customer_id(db=db, customer_id=customer_data.id)

    customer = customer_schemas.CustomerUser(**{
        "name": customer_data.name,
        "phone": customer_data.phone,
        "cpf": customer_data.cpf,
        "user_id": customer_data.user_id,
        "id": customer_data.id,
        "created_at": customer_data.created_at,
        "updated_at": customer_data.updated_at,
        "email": user_data.email,
        "username": user_data.username, 
        "professional_id": professional_data.id if professional_data else None,
        "profile_pic": customer_data.profile_pic
    })
    return customer

def get_customer(db: Session, param: str):
    customer_data = db.query(customer_models.Customer).filter(or_(customer_models.Customer.name.ilike(f"%{param}%"), customer_models.Customer.cpf.ilike(f"%{param}%"))).all()
    
    return customer_data