from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .db import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    procedure = Column(String)
    amount = Column(Integer)
    fraud_flag = Column(Boolean, default=False)
