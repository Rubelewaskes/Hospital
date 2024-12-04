from utils.repository import SQLAlchemyRepository

from sqlalchemy import insert, select, func, case
from sqlalchemy.orm import aliased
from db.database import async_session_maker

from models import (
    CheckUp, CheckUpPlace, 
    Diagnosis, Symptom,
    SymptomCheckUp, Doctor,
    )

class SQLAlchemyRepositoryCheckUp(SQLAlchemyRepository):
    async def add_new_check_up(self, check_up: dict, symptom_list: list):
        async with async_session_maker() as session:
            async with session.begin():
                session.add(check_up)
                await session.flush()
                
                for symptom in symptom_list:
                    symptom.check_up_id = check_up.id
                    session.add(symptom)
                
                return {"id" : check_up.id}

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
                select(
                    func.array_agg(
                        func.distinct(
                            case(
                                (SymptomCheckUp.symptom_id.isnot(None), Symptom.name),
                                else_=SymptomCheckUp.description
                            )
                        )
                    )
                )
                .select_from(SymptomCheckUp)
                .join(Symptom, Symptom.id == SymptomCheckUp.symptom_id, isouter=True)
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

    