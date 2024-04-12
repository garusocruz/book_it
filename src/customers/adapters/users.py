from sqlalchemy.orm import Session
from ...customers import models as customer_models, schemas as customer_schemas
from ...users import crud as user_crud

def get_customer_by_user_id(db: Session, user_id: int):
    customer_data = db.query(customer_models.Customer).filter(customer_models.Customer.user_id == user_id).first()
    user_data = user_crud.get_user(db=db, user_id=user_id)

    customer = customer_schemas.CustomerUser(**{
        "name": customer_data.name,
        "phone": customer_data.phone,
        "cpf": customer_data.cpf,
        "user_id": customer_data.user_id,
        "id": customer_data.id,
        "created_at": customer_data.created_at,
        "updated_at": customer_data.updated_at,
        "email": user_data.email,
        "username": user_data.username
    })
    return customer