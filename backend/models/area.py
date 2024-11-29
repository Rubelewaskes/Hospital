from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from db.database import Base
from schemas.area import AreaSchema, AddressAreaSchema, AreaDoctorSchema

class Area(Base):
    __tablename__ = "area"
    __table_args__ = {'schema': 'hospital'}

    doctor_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column()
    second_name: Mapped[str] = mapped_column()
    third_name: Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    experience: Mapped[int] = mapped_column()

    def to_read_model(self) -> AreaDoctorSchema:
        return DoctorSchema(
            id=self.doctor_id,
            first_name=self.first_name,
            second_name=self.second_name,
            third_name=self.third_name,
            phone_number=self.phone_number,
            experience=self.experience,
        )
    
class AddressArea(Base):
    __tablename__ = "address_area"
    __table_args__ = {'schema': 'hospital'}


    address_area_id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column()
    house: Mapped[str] = mapped_column()
    building: Mapped[str] = mapped_column()
    flat: Mapped[int] = mapped_column()
    area_id: Mapped[int] = mapped_column(ForeignKey("area.id"))

    def to_read_model(self) -> AddressAreaSchema:
        return DoctorSchema(
            id=self.address_area_id,
            street=self.street,
            house=self.house,
            building=self.building,
            flat=self.flat,
            area_id=self.area_id,
        )
    
class AreaDoctor(Base):
    __tablename__ = "area_doctor"
    __table_args__ = {'schema': 'hospital'}

    area_doctor_id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctor.id"))
    area_id: Mapped[int] = mapped_column(ForeignKey("area.id"))
    
    def to_read_model(self) -> AreaSchema:
        return DoctorSchema(
            id=self.area_doctor_id,
            doctor_id=self.doctor_id,
            area_id=self.area_id,
        )