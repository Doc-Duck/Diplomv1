from fastapi import APIRouter, Depends
from repositories.specializations import create_specialization, select_all_specializations, delete_specialization
from models.specializations import ShowSpecialization, CreateSpecialization
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from typing import List

specialization_router = APIRouter()


@specialization_router.post("/", response_model=ShowSpecialization)
async def add_specialization(body: CreateSpecialization, db: AsyncSession = Depends(get_db)) -> ShowSpecialization:
    return await create_specialization(db, body)


@specialization_router.get("/", response_model=List[ShowSpecialization])
async def show_all_specializations(db: AsyncSession = Depends(get_db)) -> List[ShowSpecialization]:
    return await select_all_specializations(db)


@specialization_router.get("/{spec_id}", response_model=object)
async def show_all_specializations(spec_id: int, db: AsyncSession = Depends(get_db)) -> object:
    return await delete_specialization(spec_id, db)

