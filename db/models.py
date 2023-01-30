from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
Base = declarative_base()


class Doctors(Base):
    __tablename__ = 'doctors'

    doctor_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(length=250), nullable=False)
    specializations = relationship("Specializations")
    appointments = relationship("Appointments")


class Appointments(Base):
    __tablename__ = 'appointments'

    appointment_id = Column(Integer, primary_key=True, index=True)
    client_full_name = Column(String(length=250), nullable=False)
    time_from = Column(DateTime(timezone=True), nullable=False)
    time_to = Column(DateTime(timezone=True), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id", ondelete='cascade'), nullable=True)


class Specializations(Base):
    __tablename__ = 'specializations'

    specialization_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=250), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id", ondelete='cascade'), nullable=True)