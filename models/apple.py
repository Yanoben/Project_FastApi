from pydantic import BaseModel


class Apple(BaseModel):
    id: int
    user_id: int
    name: str
    description: str


class AppleIn(BaseModel):
    name: str
    description: str
