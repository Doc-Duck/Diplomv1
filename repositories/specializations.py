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
                name=body.name
            )
            return ShowSpecialization(
                specialization_id=specialization.specialization_id,
                name=specialization.name,
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

# async def create_new_student(body: StudentCreate, db) -> ShowStudent:
#     async with db as session:
#         async with session.begin():
#             user_dal = StudentDAL(session)
#             user = await user_dal.create_user(
#                 name=body.name,
#                 surname=body.surname,
#                 email=body.email,
#                 project_id=body.project_id
#             )
#             return ShowStudent(
#                 student_id=user.student_id,
#                 name=user.name,
#                 surname=user.surname,
#                 email=user.email,
#                 project_id=user.project_id,
#             )
#
#
# async def patch_user(student: StudentUpdate, db) -> ShowStudent:
#     async with db as session:
#         async with session.begin():
#             student_dal = StudentDAL(session)
#             student = await student_dal.patch_user(student)
#             return ShowStudent(
#                 student_id=student.student_id,
#                 name=student.name,
#                 surname=student.surname,
#                 email=student.email,
#                 project_id=student.project_id,
#             )
#
#
# async def select_all_users(db) -> List[ShowStudent]:
#     async with db as session:
#         async with session.begin():
#             user_dal = StudentDAL(session)
#             students = await user_dal.select_users()
#             print(parse_obj_as(List[ShowStudent], students))
#             return parse_obj_as(List[ShowStudent], students)
#
#
# async def delete_student(student_id: str, db) -> object:
#     async with db as session:
#         async with session.begin():
#             student_dal = StudentDAL(session)
#             deleted_id = await student_dal.delete_student(student_id)
#             if deleted_id:
#                 return deleted_id
#             else:
#                 return {'error': 'no rows to delete'}
