# app/schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.enums import PreferenceType

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    current_preferences: Optional[PreferenceType]  # opcional, pode ser passado na criação

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(UserBase):
    id: int
    preferences: List[str]

    class Config:
        orm_mode = True
