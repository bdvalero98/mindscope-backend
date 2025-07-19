from typing import Optional

from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]

    class Config:
        orm_mode = True
