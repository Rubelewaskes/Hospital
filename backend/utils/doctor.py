from utils.repository import SQLAlchemyRepository

from sqlalchemy import insert, select, func, case
from sqlalchemy.orm import aliased
from db.database import async_session_maker
from models import AreaDoctor, Doctor
from auth.schemas import UserCreate
from fastapi_users.db import SQLAlchemyUserDatabase
from auth.db import User
from auth.users import UserManager

class SQLAlchemyRepositoryDoctor(SQLAlchemyRepository):
    async def get_all_doctors(self):
        async with async_session_maker() as session:
            stmt_doc = select(self.model)
            res = await session.execute(stmt_doc)
            rows = res.all()

            result = []

            for row in rows:
                stmt_areas = select(AreaDoctor.area_id).where(AreaDoctor.doctor_id == row[0].id)
                res_areas = await session.execute(stmt_areas)
                rows_area = res_areas.all()

                areas = []

                for row_area in rows_area:
                    areas.append(
                        {
                            "area_id": row_area[0],
                        }
                    )

                result.append(
                {
                    "doctor_id": row[0].id,
                    "first_name": row[0].first_name,
                    "second_name": row[0].second_name,
                    "third_name": row[0].third_name,
                    "phone_number": row[0].phone_number,
                    "experience": row[0].experience,
                    "areas_list": areas,
                }
                )
                
            return result 
            
            
    async def update_doctor(self, id: int, updDoctor: dict, areas_list: list):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.__table__.primary_key.columns.values()[0] == id)
            res = await session.execute(stmt)
            if obj := res.scalar_one_or_none():
                for key, value in updDoctor.items():
                    if hasattr(obj, key):
                        setattr(obj, key, value)
                

                stmt = select(AreaDoctor).filter(AreaDoctor.doctor_id == id)
                result = await session.execute(stmt)
                
                if records_to_delete := result.scalars().all():
                    for record in records_to_delete:
                        await session.delete(record)
                
                for area in areas_list:
                    session.add(area)
                
                await session.commit()
                await session.refresh(obj)

                return {col.name: getattr(obj, col.name) for col in obj.__mapper__.primary_key}
            
            raise HTTPException(
                    status_code=400,
                    detail="Object not found"
            )

    async def add_new_doctor(
        self,
        doctor: Doctor, 
        area_list: list,
        user: UserCreate
    ):
        async with async_session_maker() as session:
            user_db = SQLAlchemyUserDatabase(session, User)
            user_manager = UserManager(user_db)
            created_user = await user_manager.create(user, safe=True)

            doctor.user_id = created_user.id
            session.add(doctor)
            await session.flush()

            for area in area_list:
                area.doctor_id = doctor.id
                session.add(area)
            
            await session.commit()

        return {"id": doctor.id}