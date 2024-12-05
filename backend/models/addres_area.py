from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from db.database import Base
from schemas import AddressAreaSchema

class AddressArea(Base):
    __tablename__ = "address_area"
    __table_args__ = {'schema': 'hospital'}


    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column()
    house: Mapped[str] = mapped_column()
    building: Mapped[str] = mapped_column()
    flat: Mapped[int] = mapped_column()
    area_id: Mapped[int] = mapped_column(ForeignKey("hospital.area.id"))

    def to_read_model(self) -> AddressAreaSchema:
        return AddressAreaSchema(
            id=self.id,
            street=self.street,
            house=self.house,
            building=self.building,
            flat=self.flat,
            area_id=self.area_id,
        )