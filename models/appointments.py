from pydantic import BaseModel
from datetime import datetime


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class CreateAppointment(BaseModel):
    client_full_name: str
    time_from: datetime
    time_to: datetime


class ShowAppointment(TunedModel):
    appointment_id: int
    client_full_name: str
    time_from: datetime
    time_to: datetime
