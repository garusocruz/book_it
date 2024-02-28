from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from ..db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/places/", response_model=schemas.Place)
def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    return crud.create_place(db=db, place=place)


@app.get("/places/", response_model=list[schemas.Place])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_places(db, skip=skip, limit=limit)
    return users


@app.get("/places/{place_id}", response_model=schemas.Place)
def read_user(place_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_place(db, place_id=place_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/places/{place_id}", response_model=schemas.Place)
def update_place(place_id: int, place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = crud.update_place(db, place_id=place_id, place=place)
    if not db_place:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place

@app.delete("/places/{place_id}", response_model=schemas.Place)
def delete_place(place_id: int, db: Session = Depends(get_db)):
    db_place = crud.delete_place(db, place_id=place_id)
    if not db_place:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place