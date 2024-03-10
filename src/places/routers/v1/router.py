from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from ....users import service as user_service
from ....users import schemas as user_schema


from ... import crud, models, schemas
from ....db.database import engine, get_db
models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/v1/places", tags=["place"])


@router.post("/places/", response_model=schemas.Place)
def create_place(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    return crud.create_place(db=db, place=place)


@router.get("/places/", response_model=list[schemas.Place])
def read_users(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_places(db, skip=skip, limit=limit)
    return users


@router.get("/places/{place_id}", response_model=schemas.Place)
def read_user(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], place_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_place(db, place_id=place_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/places/{place_id}", response_model=schemas.Place)
def update_place(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], place_id: int, place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = crud.update_place(db, place_id=place_id, place=place)
    if not db_place:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place

@router.delete("/places/{place_id}", response_model=schemas.Place)
def delete_place(current_user: Annotated[user_schema.User, Depends(user_service.get_current_active_user)], place_id: int, db: Session = Depends(get_db)):
    db_place = crud.delete_place(db, place_id=place_id)
    if not db_place:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place