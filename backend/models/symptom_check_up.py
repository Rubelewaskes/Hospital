from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from schemas import SymptomCheckUpSchema

class SymptomCheckUp(Base):
    __tablename__ = "symptom_check_up"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    symptom_id: Mapped[int] = mapped_column(ForeignKey("hospital.symptom.id"))
    check_up_id: Mapped[int] = mapped_column(ForeignKey("hospital.check_up.id"))
    description: Mapped[str] = mapped_column()

    def to_read_model(self) -> SymptomCheckUpSchema:
        return DiagnosisSchema(
            id=self.diagnosis_id,
            symptom_id=self.symptom_id,
            check_up_id=self.check_up_id,
            description=self.description,
        )