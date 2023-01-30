from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Appointments
from sqlalchemy import delete
import datetime


class AppoinmentDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_appointment(self, client_name: str, dt_from: datetime.datetime,
                                 dt_to: datetime.datetime) -> Appointments:
        new_appointment = Appointments(
            client_full_name=client_name,
            time_from=dt_from,
            time_to=dt_to,
        )
        self.db_session.add(new_appointment)
        await self.db_session.flush()
        return new_appointment

    async def delete_appointment(self, appointment_id):
        result = await self.db_session.execute(
            delete(Appointments).where(Appointments.appointment_id == appointment_id).returning(
                Appointments.appointment_id))
        await self.db_session.flush()
        return {'appointment_id': result.one()[0]}
