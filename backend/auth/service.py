from db.database import async_session_maker
from sqlalchemy import select
from models import Patient, Doctor
from auth.db import User
import uuid

class AuthService():
    model = User

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
    
    async def get_patient_uid(self, id):
        async with async_session_maker() as session:
            stmt = select(Patient.user_id).where(Patient.id == id)
            res = await session.execute(stmt)
            patient_id = res.first()
            return uuid.UUID(str(patient_id[0]))

    async def get_doctor_uid(self, id):
        async with async_session_maker() as session:
            stmt = select(Doctor.user_id).where(Doctor.id == id)
            res = await session.execute(stmt)
            doctor_id = res.first()
            return uuid.UUID(str(doctor_id[0]))
    
    async def unactivate(self, uid):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.__table__.primary_key.columns.values()[0] == uid)
            res = await session.execute(stmt)
            if obj := res.scalar_one_or_none():
                if hasattr(obj, "is_active"):
                    setattr(obj, "is_active", False)

                await session.commit()
            return