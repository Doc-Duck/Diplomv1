from dals.doctors import DoctorsDAL
from models.doctors import ShowDoctors, DoctorCreate, DoctorUpdate
from pydantic import parse_obj_as
from typing import List


# POST
async def create_new_doctor(body: DoctorCreate, db) -> DoctorCreate:
    async with db as session:
        async with session.begin():
            doctor_dal = DoctorsDAL(session)
            doctor = await doctor_dal.create_doctor(
                name=body.full_name
            )
            return DoctorCreate(
                full_name=doctor.full_name
            )


# PATCH
async def patch_doctor(project: DoctorUpdate, db) -> ShowDoctors:
    async with db as session:
        async with session.begin():
            doctor_dal = DoctorsDAL(session)
            doctor = await doctor_dal.patch_doctor(project)
            return parse_obj_as(ShowDoctors, project)


# GET
async def select_all_doctors(db) -> List[ShowDoctors]:
    async with db as session:
        async with session.begin():
            doctor_dal = DoctorsDAL(session)
            doctors = await doctor_dal.select_doctors()
            print(doctors[0].appointments)
            return parse_obj_as(List[ShowDoctors], doctors)


# DELETE
async def delete_doctor(doctor_id: object, db) -> object:
    async with db as session:
        async with session.begin():
            doctor_dal = DoctorsDAL(session)
            deleted_id = await doctor_dal.delete_doctor(doctor_id)
            if deleted_id:
                return deleted_id
            else:
                return {'error': 'no rows to delete'}