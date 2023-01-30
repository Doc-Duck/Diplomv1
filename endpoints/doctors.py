from fastapi import APIRouter, Depends
from repositories.doctors import create_new_doctor, patch_doctor, select_all_doctors, delete_doctor
from models.doctors import ShowDoctors, DoctorCreate, DoctorUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from typing import List

doctors_router = APIRouter()


@doctors_router.post("/", response_model=DoctorCreate)
async def add_doctor(body: DoctorCreate, db: AsyncSession = Depends(get_db)) -> DoctorCreate:
    return await create_new_doctor(body, db)


@doctors_router.patch("/", response_model=ShowDoctors)
async def patch_pr(body: DoctorUpdate, db: AsyncSession = Depends(get_db)) -> ShowDoctors:
    return await patch_doctor(body, db)


@doctors_router.delete("/{doctor_id}", response_model=object)
async def remove_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)) -> object:
    return await delete_doctor(doctor_id, db)


@doctors_router.get("/", response_model=List[ShowDoctors])
async def show_projects(db: AsyncSession = Depends(get_db)) -> List[ShowDoctors]:
    return await select_all_doctors(db)
