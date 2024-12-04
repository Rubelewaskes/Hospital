from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from schemas.gender import GenderSchema

class Gender(Base):
    __tablename__ = "gender"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column()

    def to_read_model(self) -> GenderSchema:
        return GenderSchema(
            id=self.id,
            description=self.description,
        )