from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from schemas import CheckUpPlaceSchema

class CheckUpPlace(Base):
    __tablename__ = "check_up_place"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    place: Mapped[str] = mapped_column()

    def to_read_model(self) -> CheckUpPlaceSchema:
        return CheckUpPlaceSchema(
            id=self.id,
            place=self.place,
        )