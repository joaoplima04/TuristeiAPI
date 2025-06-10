# schemas.py
from pydantic import BaseModel

class PreferenceBase(BaseModel):
    name: str

class PreferenceOut(PreferenceBase):
    id: int

    class Config:
        orm_mode = True
