from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from sqlalchemy.dialects.postgresql import UUID
import uuid

from db.database import Base
from schemas.patient import PatientSchema


class Patient(Base):
    __tablename__ = "patient"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column()
    second_name: Mapped[str] = mapped_column()
    third_name: Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    address_id: Mapped[int] = mapped_column(ForeignKey("hospital.address_area.id"))
    born_date: Mapped[date] = mapped_column()
    gender_id: Mapped[int] = mapped_column(ForeignKey("hospital.gender.id"))
    user_id: Mapped[uuid.UUID] = mapped_column()


    def to_read_model(self) -> PatientSchema:
        return PatientSchema(
            id=self.id,
            first_name=self.first_name,
            second_name=self.second_name,
            third_name=self.third_name,
            phone_number=self.phone_number,
            address_id=self.address_id,
            born_date=self.born_date,
            gender_id=self.gender_id,
            user_id=self.user_id,
        )