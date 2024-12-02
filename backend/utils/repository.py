from abc import ABC, abstractmethod
from sqlalchemy import insert, select, func
from sqlalchemy.orm import aliased
from db.database import async_session_maker

from models import (
    CheckUp, CheckUpPlace, 
    Diagnosis, Symptom,
    SymptomCheckUp, Patient,
    Area, AddressArea, 
    AreaDoctor, Gender,
    Doctor,
    )


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    @abstractmethod
    async def find_one():
        raise NotImplementedError



class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            session.add(data)
            await session.commit()
            await session.refresh(data)
            return {col.name: getattr(data, col.name) for col in data.__mapper__.primary_key}
    
    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
    
    async def find_one(self, id):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.__table__.primary_key.columns.values()[0] == id)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
    
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


class SQLAlchemyRepositoryCheckUp(SQLAlchemyRepository):
    async def get_all_short_checkup(self, id):
        async with async_session_maker() as session:
            stmt = (
                select(
                    CheckUp.id,
                    CheckUpPlace.place,
                    CheckUp.check_up_date,
                    func.concat(Doctor.first_name, ' ', Doctor.second_name, ' ', Doctor.third_name).label('doctor_FIO'),
                    Diagnosis.name
                )
                .join(Doctor, Doctor.id == CheckUp.doctor_id)
                .join(CheckUpPlace, CheckUpPlace.id == CheckUp.check_up_place_id)
                .outerjoin(Diagnosis, Diagnosis.id == CheckUp.diagnosis_id)
                .where(CheckUp.patient_id == id)
            )
            res = await session.execute(stmt)
            rows = res.all()
            result = [
            {
                "check_up_id": row[0],
                "place": row[1],
                "check_up_date": row[2],
                "doctor_FIO": row[3],
                "diagnosis": row[4],
            }
            for row in rows
        ]
            return result


    async def get_check_up(self, id):
        async with async_session_maker() as session:
            subquery_symptoms = (
                select(func.array_agg(func.distinct(Symptom.name)))
                .join(SymptomCheckUp, Symptom.id == SymptomCheckUp.symptom_id)
                .where(SymptomCheckUp.check_up_id == id)
                .scalar_subquery()
            )

            stmt = (
                select(
                    CheckUp.id,
                    CheckUpPlace.place,
                    CheckUp.check_up_date,
                    func.concat(
                        Doctor.first_name, ' ', Doctor.second_name, ' ', Doctor.third_name
                    ).label('doctor_FIO'),
                    Diagnosis.name,
                    CheckUp.prescription,
                    subquery_symptoms.label("symptoms"),
                )
                .join(Doctor, Doctor.id == CheckUp.doctor_id)
                .join(CheckUpPlace, CheckUpPlace.id == CheckUp.check_up_place_id)
                .outerjoin(Diagnosis, Diagnosis.id == CheckUp.diagnosis_id)
                .where(CheckUp.id == id)
            )

            res = await session.execute(stmt)
            
            if row := res.first():
                result = {
                    "check_up_id": row[0],
                    "place": row[1],
                    "check_up_date": row[2],
                    "doctor_FIO": row[3],
                    "diagnosis": row[4],
                    "prescription": row[5],
                    "symptoms": row[6],
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