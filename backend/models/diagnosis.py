from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from schemas import DiagnosisSchema
    
class Diagnosis(Base):
    __tablename__ = "diagnosis"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    def to_read_model(self) -> DiagnosisSchema:
        return DiagnosisSchema(
            id=self.id,
            name=self.name,
        )