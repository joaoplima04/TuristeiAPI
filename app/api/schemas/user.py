from pydantic import BaseModel, EmailStr
from typing import List, Optional


# Schema para representar a preferência
class PreferenceBase(BaseModel):
    name: str

class PreferenceOut(PreferenceBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    preferences: Optional[List[str]] = []  # nomes das preferências


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(UserBase):
    id: int
    preferences: List[PreferenceOut]

    class Config:
        orm_mode = True
