from utils.repository import SQLAlchemyRepository

from sqlalchemy import insert, select, func
from sqlalchemy.orm import aliased
from db.database import async_session_maker

from models import (
    Patient, Area, 
    AddressArea, AreaDoctor, 
    Gender, Doctor,
    )

class SQLAlchemyRepositoryPatient(SQLAlchemyRepository):
    async def find_address(self, data: dict):
        async with async_session_maker() as session:
            stmt = (
                    select(self.model)
                    .where(self.model.street == data.street and 
                    self.model.house == data.house and
                    self.model.building == data.building and
                    self.model.flat == data.flat)
                )
            res = await session.execute(stmt)
            if row := res.first():
                result = {
                    "address_id": row[0].id,
                }
                return result
            return None
            
    async def get_all_patients_on_doctor_area(self, id):
        async with async_session_maker() as session:
            stmt = (
                select(
                    Patient.id,
                    func.concat(
                        Patient.first_name, ' ', Patient.second_name, ' ', Patient.third_name
                    ).label('Patient_FIO'),
                    Gender.description,
                    Patient.born_date,
                    Patient.phone_number,
                )
                .outerjoin(AddressArea, AddressArea.id == Patient.address_id)
                .outerjoin(Area, Area.id == AddressArea.area_id)
                .outerjoin(AreaDoctor, Area.id == AreaDoctor.area_id )
                .outerjoin(Doctor, Doctor.id == AreaDoctor.doctor_id)
                .join(Gender, Gender.id == Patient.gender_id)
                .where(Doctor.id == id)
            )

            res = await session.execute(stmt)

            if rows := res.all():
                result = [{
                    "patient_id": row[0],
                    "patient_FIO": row[1],
                    "gender": row[2],
                    "born_date": row[3],
                    "phone_number": row[4],
                }
                    for row in rows
                ]
                return result
            return None