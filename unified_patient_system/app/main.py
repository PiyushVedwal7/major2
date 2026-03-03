from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .db import engine, Base, SessionLocal
from . import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Unified Patient System")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Hospital Unified Data System Running"}


# Create Patient
@app.post("/patients/")
def create_patient(patient: schemas.PatientCreate,
                   db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)


# Add Claim
@app.post("/claims/")
def add_claim(claim: schemas.ClaimCreate,
              db: Session = Depends(get_db)):
    return crud.create_claim(db, claim)
