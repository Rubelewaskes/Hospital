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
    async def get_one_full(self, id):
        async with async_session_maker() as session:
            stmt = (
                select (self.model.first_name, self.model.second_name,
                self.model.third_name, self.model.phone_number,
                AddressArea.street, AddressArea.house, 
                AddressArea.building, AddressArea.flat,
                Gender.description, self.model.born_date
                )
                .join(AddressArea, AddressArea.id == self.model.address_id)
                .join(Gender, Gender.id == self.model.gender_id)
                .where(self.model.id == id)
            )

            res = await session.execute(stmt)

            if row := res.first():
                result = {
                    "first_name": row[0],
                    "second_name": row[1],
                    "third_name": row[2],
                    "phone_number": row[3],
                    "address": {
                        "street": row[4],
                        "house": row[5],
                        "building": row[6],
                        "flat": row[7],
                        },
                    "gender": row[8],
                    "born_date": row[9],
                }
                return result
            
            return None

    async def get_all_full(self):
        async with async_session_maker() as session:
            stmt = (
                select (self.model.first_name, self.model.second_name,
                self.model.third_name, self.model.phone_number,
                AddressArea.street, AddressArea.house, 
                AddressArea.building, AddressArea.flat,
                Gender.description, self.model.born_date
                )
                .join(AddressArea, AddressArea.id == self.model.address_id)
                .join(Gender, Gender.id == self.model.gender_id)
            )

            res = await session.execute(stmt)
            rows =  res.all()

            result = []

            for row in rows:
                result.append({
                    "first_name": row[0],
                    "second_name": row[1],
                    "third_name": row[2],
                    "phone_number": row[3],
                    "address": {
                        "street": row[4],
                        "house": row[5],
                        "building": row[6],
                        "flat": row[7],
                        },
                    "gender": row[8],
                    "born_date": row[9],
                })
            
            return result
            

    async def find_address(self, data: dict):
        async with async_session_maker() as session:
            stmt = (
                    select(self.model)
                    .where((self.model.street == data.street) & 
                        (self.model.house == data.house) & 
                        (self.model.building == data.building) & 
                        (self.model.flat == data.flat)
                    )
                )
            res = await session.execute(stmt)
            if row := res.first():
                print(row[0].id)
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