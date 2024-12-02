from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from db.database import Base
from schemas.check_up import CheckUpSchema


class CheckUp(Base):
    __tablename__ = "check_up"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    check_up_place_id: Mapped[int] = mapped_column(ForeignKey("hospital.check_up_place.id"))
    check_up_date: Mapped[date] = mapped_column()
    doctor_id: Mapped[int] = mapped_column(ForeignKey("hospital.doctor.id"))
    patient_id: Mapped[int] = mapped_column(ForeignKey("hospital.patient.id"))
    diagnosis_id: Mapped[int] = mapped_column(ForeignKey("hospital.diagnosis.id"))
    prescription: Mapped[str] = mapped_column()

    def to_read_model(self) -> CheckUpSchema:
        return CheckUpSchema(
            id=self.id,
            check_up_place_id=self.check_up_place_id,
            check_up_date=self.check_up_date,
            doctor_id=self.doctor_id,
            patient_id=self.patient_id,
            diagnosis_id=self.diagnosis_id,
            prescription=self.prescription,
        )