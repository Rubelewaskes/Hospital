from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from fastapi_users.exceptions import UserAlreadyExists, InvalidPasswordException

from utils.repository import SQLAlchemyRepository
from sqlalchemy import insert, select, func
from sqlalchemy.orm import aliased
from db.database import async_session_maker
from auth.schemas import UserCreate
from fastapi_users.db import SQLAlchemyUserDatabase
from auth.db import User
from auth.users import UserManager

from models import (
    Patient, Area, 
    AddressArea, AreaDoctor, 
    Gender, Doctor,
    )

class SQLAlchemyRepositoryPatient(SQLAlchemyRepository):
    async def get_one_full(self, id):
         async with async_session_maker() as session:
            stmt = (
                select (self.model.id, self.model.first_name, self.model.second_name,
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
                    "patient_id": row[0],
                    "first_name": row[1],
                    "second_name": row[2],
                    "third_name": row[3],
                    "phone_number": row[4],
                    "address":{
                        "street": row[5],
                        "house": row[6],
                        "building": row[7],
                        "flat": row[8],
                    },
                    "description": row[9],
                    "born_date": row[10],
                }
            
            return result

    async def get_all_full(self):
        async with async_session_maker() as session:
            stmt = (
                select (self.model.id, self.model.first_name, self.model.second_name,
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
                    "patient_id": row[0],
                    "first_name": row[1],
                    "second_name": row[2],
                    "third_name": row[3],
                    "phone_number": row[4],
                    "street": row[5],
                    "house": row[6],
                    "building": row[7],
                    "flat": row[8],
                    "description": row[9],
                    "born_date": row[10],
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
                    Patient.first_name, 
                    Patient.second_name, 
                    Patient.third_name,
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
                    "first_name": row[1],
                    "second_name": row[2],
                    "third_name": row[3],
                    "gender": row[4],
                    "born_date": row[5],
                    "phone_number": row[6],
                }
                    for row in rows
                ]
                return result
            return None
    


    async def add_patient_user(
            self, 
            patient: Patient,
            user: UserCreate,
        ):
        async with async_session_maker() as session:
            try:
                session.add(patient)
                await session.flush()

                user_db = SQLAlchemyUserDatabase(session, User)
                user_manager = UserManager(user_db)

                created_user = await user_manager.create(user, safe=True)

                patient.user_id = created_user.id
                await session.commit()

                await session.refresh(patient)
                return {"id": patient.id}

            except (SQLAlchemyError, InvalidPasswordException, UserAlreadyExists) as e:
                await session.rollback()
                raise HTTPException(status_code=400, detail=str(e))
