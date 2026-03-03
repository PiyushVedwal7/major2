from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str


class ClaimCreate(BaseModel):
    patient_id: int
    procedure: str
    amount: int
