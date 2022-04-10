from fastapi import HTTPException, status
from typing import List, Optional
from models.apple import Apple, AppleIn
from db.apples import apples
from .base import BaseRepository


class AppleRepository(BaseRepository):

    async def create(self, user_id: int, a: AppleIn, user_role: str) -> Apple:
        if user_role == "salesman":
            apple = Apple(
                id=0,
                user_id=user_id,
                name=a.name,
                description=a.description,
            )
            values = {**apple.dict()}
            values.pop("id", None)
            query = apples.insert().values(**values)
            apple.id = await self.database.execute(query=query)
            return apple
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Apple]:
        query = apples.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = apples.delete().where(apples.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Apple]:
        query = apples.select().where(apples.c.id == id)
        apple = await self.database.fetch_one(query=query)
        if apple is None:
            return None
        return Apple.parse_obj(apple)


class AppleBuyRepository(BaseRepository):
    pass
