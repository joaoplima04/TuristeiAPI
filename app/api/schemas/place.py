from pydantic import BaseModel
from typing import List, Optional


# Novo schema base para Preference
class PreferenceBase(BaseModel):
    name: str

class PreferenceOut(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PlaceBase(BaseModel):
    name: str
    city: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    image_url: Optional[str] = None


# Schema de criação: aceita lista de nomes das preferências
class PlaceCreate(PlaceBase):
    preferences: List[str]  # nomes das preferências


# Schema de resposta: retorna lista de nomes das preferências
class PlaceOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    image_url: Optional[str] = None
    preferences: List[PreferenceOut]  # nomes das preferências associadas

    class Config:
        orm_mode = True
