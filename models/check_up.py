from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from db.database import Base
from schemas.check_up import (
    CheckUpSchema, 
    CheckUpPlaceSchema, 
    DiagnosisSchema,
    SymptomSchema,
    SymptomCheckUpSchema,
    )


class CheckUp(Base):
    __tablename__ = "check_up"
    __table_args__ = {'schema': 'hospital'}

    check_up_id: Mapped[int] = mapped_column(primary_key=True)
    check_up_place_id: Mapped[int] = mapped_column(ForeignKey("check_up_place.id"))
    check_up_date: Mapped[date] = mapped_column()
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctor.id"))
    patient_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    diagnosis_id: Mapped[int] = mapped_column(ForeignKey("diagnosis.id"))
    prescription: Mapped[str] = mapped_column()
    
    
    # assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def to_read_model(self) -> CheckUpSchema:
        return CheckUpSchema(
            id=self.check_up_id,
            check_up_place_id=self.check_up_place_id,
            check_up_date=self.check_up_date,
            doctor_id=self.doctor_id,
            patient_id=self.patient_id,
            diagnosis_id=self.diagnosis_id,
            prescription=self.prescription,
        )

class CheckUpPlace(Base):
    __tablename__ = "check_up_place"
    __table_args__ = {'schema': 'hospital'}

    check_up_place_id: Mapped[int] = mapped_column(primary_key=True)
    place: Mapped[str] = mapped_column()
    
    # assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def to_read_model(self) -> CheckUpPlaceSchema:
        return CheckUpPlaceSchema(
            id=self.check_up_place_id,
            place=self.place,
        )

class Diagnosis(Base):
    __tablename__ = "diagnosis"
    __table_args__ = {'schema': 'hospital'}

    diagnosis_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    def to_read_model(self) -> DiagnosisSchema:
        return DiagnosisSchema(
            id=self.diagnosis_id,
            name=self.name,
        )

class Symptom(Base):
    __tablename__ = "symptom"
    __table_args__ = {'schema': 'hospital'}

    symptom_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    def to_read_model(self) -> SymptomSchema:
        return SymptomSchema(
            id=self.symptom_id,
            name=self.name,
        )

class SymptomCheckUp(Base):
    __tablename__ = "symptom_check_up"
    __table_args__ = {'schema': 'hospital'}

    symptom_check_up_id: Mapped[int] = mapped_column(primary_key=True)
    symptom_id: Mapped[int] = mapped_column(ForeignKey("symptom.id"))
    check_up_id: Mapped[int] = mapped_column(ForeignKey("check_up.id"))
    description: Mapped[str] = mapped_column()

    def to_read_model(self) -> DiagnosisSchema:
        return DiagnosisSchema(
            id=self.diagnosis_id,
            symptom_id=self.symptom_id,
            check_up_id=self.check_up_id,
            name=self.name,
        )