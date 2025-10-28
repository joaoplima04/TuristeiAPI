# schemas.py
from pydantic import BaseModel
from typing import List

class PreferenceBase(BaseModel):
    name: str

class PreferenceOut(PreferenceBase):
    id: int

    class Config:
        orm_mode = True

class SaveUserPreferences(BaseModel):
    user_id: int
    preferences: List[str] 