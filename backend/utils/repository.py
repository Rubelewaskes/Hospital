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



class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            session.add(data)
            await session.commit()
            await session.refresh(data)
            return {col.name: getattr(data, col.name) for col in data.__mapper__.primary_key}

    async def update_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            pass
    
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
    



