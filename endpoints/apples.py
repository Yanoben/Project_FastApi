from typing import List
from models.apple import Apple, AppleIn
from models.user import User
from repositories.apples import AppleRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_apple_repository, get_current_user

router = APIRouter()


@router.get("/", response_model=List[Apple])
async def get_apples(limit: int = 100,
                     apples: AppleRepository = Depends(get_apple_repository)):
    return await apples.get_all(limit=limit)


@router.post("/", response_model=Apple)
async def create_apple(a: AppleIn,
                       apples: AppleRepository = Depends(get_apple_repository),
                       current_user: User = Depends(get_current_user)):
    print(current_user.role)
    return await apples.create(
        user_id=current_user.id, a=a, user_role=current_user.role)


# @router.put("/", response_model=Apple)
# async def update_apple(
#     id: int,
#     a: AppleIn,
#     apples: AppleRepository = Depends(get_apple_repository),
#     current_user: User = Depends(get_current_user)):
#     apple = await apples.get_by_id(id=id)
#     if apple is None or apple.user_id != current_user.id:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Apple not found")
#     return await apples.update(id=id, user_id=current_user.id, a=a)


@router.delete("/")
async def delete_apple(id: int,
                       apples: AppleRepository = Depends(get_apple_repository),
                       current_user: User = Depends(get_current_user)):
    if current_user.role != "salesman":
        await apples.get_by_id(id=id)
        await apples.delete(id=id)
        return {"status": "Delete apple successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to delete apples")


@router.get("/{id}/buy")
async def buy_apple(id: int,
                    apples: AppleRepository = Depends(get_apple_repository),
                    current_user: User = Depends(get_current_user)):
    if current_user.role != "salesman":
        if apples is None:
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
