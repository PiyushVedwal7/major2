from sqlalchemy.orm import Session
from . import models


# Create Patient
def create_patient(db: Session, patient):
    db_patient = models.Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


# Fraud Rule
def fraud_check(amount):
    return amount > 50000


# Add Claim
def create_claim(db: Session, claim):
    fraud = fraud_check(claim.amount)

    db_claim = models.Claim(
        patient_id=claim.patient_id,
        procedure=claim.procedure,
        amount=claim.amount,
        fraud_flag=fraud
    )

    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)

    return db_claim
