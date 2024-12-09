from abc import ABC, abstractmethod
from sqlalchemy import insert, select, func
from sqlalchemy.orm import aliased
from db.database import async_session_maker



class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def update_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    @abstractmethod
    async def find_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_one_uid():
        raise NotImplementedError



class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> dict:
        async with async_session_maker() as session:
            session.add(data)
            await session.commit()
            await session.refresh(data)
            return {col.name: getattr(data, col.name) for col in data.__mapper__.primary_key}


    async def update_one(self, id: int, data: dict) -> dict:
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.__table__.primary_key.columns.values()[0] == id)
            res = await session.execute(stmt)
            if obj := res.scalar_one_or_none():
                for key, value in data.items():
                    if hasattr(obj, key):
                        setattr(obj, key, value)

                await session.commit()
                await session.refresh(obj)

                return {col.name: getattr(obj, col.name) for col in obj.__mapper__.primary_key}
            
            raise HTTPException(
                    status_code=400,
                    detail="Object not found"
                )


    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
    
    async def find_one(self, id):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.__table__.primary_key.columns.values()[0] == id)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
    
    async def find_one_uid(self, uid):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.user_id == uid)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
    



