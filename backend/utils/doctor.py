from utils.repository import SQLAlchemyRepository

from sqlalchemy import insert, select, func, case
from sqlalchemy.orm import aliased
from db.database import async_session_maker

class SQLAlchemyRepositoryDoctor(SQLAlchemyRepository):
    async def add_new_doctor(self, doctor: dict, area_list: list):
        async with async_session_maker() as session:
            async with session.begin():
                session.add(doctor)
                await session.flush()
                
                for area in area_list:
                    area.doctor_id = doctor.id
                    session.add(area)
                
                return {"id" : doctor.id}