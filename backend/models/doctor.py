from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from db.database import Base
from schemas.doctor import DoctorSchema

class Doctor(Base):
    __tablename__ = "doctor"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column()
    second_name: Mapped[str] = mapped_column()
    third_name: Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    experience: Mapped[int] = mapped_column()

    def to_read_model(self) -> DoctorSchema:
        return DoctorSchema(
            id=self.id,
            first_name=self.first_name,
            second_name=self.second_name,
            third_name=self.third_name,
            phone_number=self.phone_number,
            experience=self.experience,
        )