from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    role: str


class UserIn(BaseModel):
    name: str
    email: EmailStr
    role: str
    password: constr(min_length=8)
    password2: str

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v
