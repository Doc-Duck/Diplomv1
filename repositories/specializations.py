from dals.specializations import SpecializationDAL
from models.specializations import CreateSpecialization, ShowSpecialization
from pydantic import parse_obj_as
from typing import List


# POST
async def create_specialization(db, body: CreateSpecialization):
    async with db as session:
        async with session.begin():
            spec_dal = SpecializationDAL(session)
            specialization = await spec_dal.create_specialization(
                name=body.name,
                doctor_id=body.doctor_id,
            )
            return ShowSpecialization(
                specialization_id=specialization.specialization_id,
                name=specialization.name,
                doctor_id=body.doctor_id,
            )


# GET
async def select_all_specializations(db):
    async with db as session:
        async with session.begin():
            spec_dal = SpecializationDAL(session)
            specializations = await spec_dal.select_specializations()
            return parse_obj_as(List[ShowSpecialization], specializations)


# DELETE
async def delete_specialization(spec_id: int, db) -> object:
    async with db as session:
        async with session.begin():
            spec_dal = SpecializationDAL(session)
            deleted_id = await spec_dal.delete_specialization(spec_id)
            if deleted_id:
                return deleted_id
            else:
                return {'error': 'no rows to delete'}
