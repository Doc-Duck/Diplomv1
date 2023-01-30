from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Specializations
from sqlalchemy import select, delete


class SpecializationDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_specialization(self, name: str) -> Specializations:
        new_specialization = Specializations(
            name=name
        )
        print(new_specialization)
        self.db_session.add(new_specialization)
        await self.db_session.flush()
        return new_specialization

    async def select_specializations(self):
        result = await self.db_session.execute(select(Specializations))
        return result.scalars().all()

    async def patch_specialization(self, specialization):
        db_specialization = await self.db_session.execute(select(Specializations).filter(Specializations.specialization_id == specialization.specialization_id))
        db_specialization = db_specialization.scalar()
        if db_specialization is None:
            return None

        for var, value in vars(db_specialization).items():
            setattr(db_specialization, var, value) if value else None

        self.db_session.add(db_specialization)
        await self.db_session.flush()
        return db_specialization

    async def delete_specialization(self, specialization_id):
        result = await self.db_session.execute(delete(Specializations).where(Specializations.specialization_id == specialization_id).returning(Specializations.specialization_id))
        await self.db_session.flush()
        return {'specialization_id': result.one()[0]}