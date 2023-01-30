from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class ShowSpecialization(TunedModel):
    specialization_id: int
    name: str


class CreateSpecialization(BaseModel):
    name: str

