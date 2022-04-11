from typing import List
from models.apple import Apple
from models.user import User
from repositories.apples import AppleRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_apple_repository, get_current_user

router = APIRouter()


@router.get("/")
async def buy_apple(id: int,
                    apples: AppleRepository = Depends(get_apple_repository),
                    current_user: User = Depends(get_current_user)):
    if current_user.role != "salesman":
        if await apples.get_all() == []:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Apple not found")
        await apples.get_by_id(id=id)
        await apples.delete(id=id)
        return {"status": "Bought!"}
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to buy apples")
