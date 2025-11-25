from pydantic import BaseModel
from typing import Optional

class AttractionRequestCreate(BaseModel):
    name: str
    city: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    user_id: int

class AttractionRequestOut(BaseModel):
    id: int
    name: str
    city: str
    description: Optional[str]
    latitude: float
    longitude: float
    status: str
    user_id: int

    class Config:
        orm_mode = True
