from dals.appointments import AppoinmentDAL
from models.appointments import CreateAppointment, ShowAppointment


# POST
async def create_appointment(db, body: CreateAppointment):
    async with db as session:
        async with session.begin():
            appo_dal = AppoinmentDAL(session)
            appointment = await appo_dal.create_appointment(
                client_name=body.client_full_name,
                dt_from=body.time_from,
                dt_to=body.time_to
            )
            return ShowAppointment(
                appointment_id=appointment.appointment_id,
                client_full_name=appointment.client_full_name,
                time_from=appointment.time_from,
                time_to=appointment.time_to,
            )
