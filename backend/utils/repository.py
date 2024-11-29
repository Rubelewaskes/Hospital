from abc import ABC, abstractmethod
from sqlalchemy import insert, select, func
from sqlalchemy.orm import aliased
from db.database import async_session_maker

from models.check_up import (
    CheckUp, 
    CheckUpPlace, 
    Diagnosis,
    Symptom,
    SymptomCheckUp,
    )
from models.patient import Patient
from models.area import Area, AddressArea, AreaDoctor
from models.doctor import Doctor



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
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
    
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
    
    

class SQLAlchemyRepositoryCheckUp(SQLAlchemyRepository):
    async def get_all_short_checkup(self, id):
        async with async_session_maker() as session:
            stmt = (
                select(
                    CheckUp.check_up_id,
                    CheckUpPlace.place,
                    CheckUp.check_up_date,
                    func.concat(Doctor.first_name, ' ', Doctor.second_name, ' ', Doctor.third_name).label('doctor_FIO'),
                    Diagnosis.name
                )
                .join(Doctor, Doctor.doctor_id == CheckUp.doctor_id)
                .join(CheckUpPlace, CheckUpPlace.check_up_place_id == CheckUp.check_up_place_id)
                .outerjoin(Diagnosis, Diagnosis.diagnosis_id == CheckUp.diagnosis_id)
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
                .join(SymptomCheckUp, SymptomCheckUp.symptom_id == Symptom.symptom_id)
                .where(SymptomCheckUp.check_up_id == id)
                .scalar_subquery()
            )

            stmt = (
                select(
                    CheckUp.check_up_id,
                    CheckUpPlace.place,
                    CheckUp.check_up_date,
                    func.concat(
                        Doctor.first_name, ' ', Doctor.second_name, ' ', Doctor.third_name
                    ).label('doctor_FIO'),
                    Diagnosis.name,
                    CheckUp.prescription,
                    subquery_symptoms.label("symptoms"),
                )
                .join(Doctor, Doctor.doctor_id == CheckUp.doctor_id)
                .join(CheckUpPlace, CheckUpPlace.check_up_place_id == CheckUp.check_up_place_id)
                .outerjoin(Diagnosis, Diagnosis.diagnosis_id == CheckUp.diagnosis_id)
                .where(CheckUp.check_up_id == id)
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
                    Patient.patient_id,
                    func.concat(
                        Patient.first_name, ' ', Patient.second_name, ' ', Patient.third_name
                    ).label('Patient_FIO'),
                    Patient.born_date,
                    Patient.phone_number,
                )
                .outerjoin(AddressArea, AddressArea.address_id == Patient.address_id)
                .outerjoin(Area, Area.area_id == AddressArea.area_id)
                .outerjoin(AreaDoctor, AreaDoctor.area_id == Area.area_id)
                .outerjoin(Doctor, Doctor.doctor_id == AreaDoctor.doctor_id)
                .where(Doctor.doctor_id == id)
            )

            res = await session.execute(stmt)

            if rows := res.all():
                result = [{
                    "patient_id": row[0],
                    "patient_FIO": row[1],
                    "born_date": row[2],
                    "phone_number": row[3],
                }
                    for row in rows
                ]
                return result
            return None