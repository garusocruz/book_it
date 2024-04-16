from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from ....users import service as user_service
from ....users import schemas as user_schema

from ... import crud, models, schemas
from ....db.database import engine, get_db
from fastapi import APIRouter, Response, status
models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/v1/professionals", tags=["professional"])



@router.post("/", response_model=schemas.Professional)
def create_schedule(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], professional: schemas.ProfessionalCreate, db: Session = Depends(get_db)):
    return crud.create_professioanl(db=db, professional=professional)


@router.get("/", response_model=list[schemas.Professional])
def read_schedules(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_professionals(db, skip=skip, limit=limit)
    return users


@router.get("/{professional_id}", response_model=schemas.Professional)
def read_schedule(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], professional_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.get_professional(db, professional_id=professional_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Professional not found")
    return db_schedule


@router.put("/{professional_id}", response_model=schemas.Professional)
def update_place(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], professional_id: int, professional: schemas.ProfessionalCreate, db: Session = Depends(get_db)):
    db_schedule = crud.update_professional(db, professional_id=professional_id, professional=professional)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Professional not found")
    return db_schedule

@router.delete("/{professional_id}", response_model=schemas.Professional)
def delete_place(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], professional_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.delete_professional(db, professional_id=professional_id)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Professional not found")
    return db_schedule