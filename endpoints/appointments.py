from fastapi import APIRouter, Depends
from repositories.appointments import create_appointment
from models.appointments import ShowAppointment, CreateAppointment
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db

appointment_router = APIRouter()


@appointment_router.post("/", response_model=ShowAppointment)
async def add_appointment(body: CreateAppointment, db: AsyncSession = Depends(get_db)) -> ShowAppointment:
    return await create_appointment(db, body)
