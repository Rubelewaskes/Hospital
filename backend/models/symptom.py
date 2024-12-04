from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from schemas import SymptomSchema

class Symptom(Base):
    __tablename__ = "symptom"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    def to_read_model(self) -> SymptomSchema:
        return SymptomSchema(
            id=self.id,
            name=self.name,
        )