from pydantic import BaseModel
from .specializations import ShowSpecialization
from .appointments import ShowAppointment
from typing import List, Optional


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class ShowDoctors(TunedModel):
    doctor_id: int
    full_name: str
    specializations: Optional[List[ShowSpecialization]]
    appointments: Optional[List[ShowAppointment]]


class DoctorUpdate(TunedModel):
    doctor_id: int
    full_name: Optional[str]
    specializations: Optional[List[ShowSpecialization]]
    appointments: Optional[List[ShowAppointment]]


class DoctorCreate(BaseModel):
    full_name: str
