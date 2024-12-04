from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from db.database import Base
from schemas import AreaDoctorSchema

class AreaDoctor(Base):
    __tablename__ = "area_doctor"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("hospital.doctor.id"))
    area_id: Mapped[int] = mapped_column(ForeignKey("hospital.area.id"))
    
    def to_read_model(self) -> AreaDoctorSchema:
        return DoctorSchema(
            id=self.id,
            doctor_id=self.doctor_id,
            area_id=self.area_id,
        )