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


@app.post("/professionals/", response_model=schemas.Professional)
def create_schedule(professional: schemas.ProfessionalCreate, db: Session = Depends(get_db)):
    return crud.create_professioanl(db=db, professional=professional)


@app.get("/professionals/", response_model=list[schemas.Professional])
def read_schedules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_professionals(db, skip=skip, limit=limit)
    return users


@app.get("/professionals/{professional_id}", response_model=schemas.Professional)
def read_schedule(professional_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.get_professional(db, professional_id=professional_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Professional not found")
    return db_schedule


@app.put("/professionals/{professional_id}", response_model=schemas.Professional)
def update_place(professional_id: int, professional: schemas.ProfessionalCreate, db: Session = Depends(get_db)):
    db_schedule = crud.update_professional(db, professional_id=professional_id, professional=professional)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Professional not found")
    return db_schedule

@app.delete("/professionals/{professional_id}", response_model=schemas.Professional)
def delete_place(professional_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.delete_professional(db, professional_id=professional_id)
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Professional not found")
    return db_schedule