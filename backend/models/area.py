from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base
from schemas import AreaSchema

class Area(Base):
    __tablename__ = "area"
    __table_args__ = {'schema': 'hospital'}

    id: Mapped[int] = mapped_column(primary_key=True)

    def to_read_model(self) -> AreaSchema:
        return AreaSchema(
            id=self.id,
        )
    
