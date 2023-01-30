from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Doctors
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload, joinedload


class DoctorsDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_doctor(self, name: str) -> Doctors:
        new_doctor = Doctors(
            full_name=name,
        )
        self.db_session.add(new_doctor)
        await self.db_session.flush()
        return new_doctor

    async def select_doctors(self):
        result = await self.db_session.execute(select(Doctors).options(selectinload(Doctors.appointments), selectinload(Doctors.specializations)))
        return result.scalars().all()

    async def patch_doctor(self, doctor):
        db_doctor = await self.db_session.execute(
            select(Doctors).options(
                joinedload(Doctors.specializations),
                joinedload(Doctors.appointments)
            ).filter(Doctors.doctor_id == doctor.doctor_id)
        )
        db_doctor = db_doctor.scalar()
        if db_doctor is None:
            return None

        for var, value in vars(doctor).items():
            setattr(db_doctor, var, value) if value else None

        self.db_session.add(db_doctor)
        await self.db_session.flush()
        return db_doctor

    async def delete_doctor(self, doctor_id):
        result = await self.db_session.execute(
            delete(Doctors).where(Doctors.doctor_id == doctor_id).returning(Doctors.doctor_id))
        await self.db_session.flush()
        return {'doctor_id': result.one()[0]}
