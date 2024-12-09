from db.database import async_session_maker
from sqlalchemy import select
from models import Patient, Doctor

class AuthService():
    async def get_patient_id(self, uid):
        async with async_session_maker() as session:
            stmt = select(Patient.id).where(Patient.user_id == uid)
            res = await session.execute(stmt)
            patient_id = res.first()
            return int(patient_id[0])

    async def get_doctor_id(self, uid):
        async with async_session_maker() as session:
            stmt = select(Doctor.id).where(Doctor.user_id == uid)
            res = await session.execute(stmt)
            doctor_id = res.first()
            return int(doctor_id[0])