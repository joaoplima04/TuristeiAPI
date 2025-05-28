from pydantic import BaseModel
from typing import List


class TypeBase(BaseModel):
    name: str

class TypeOut(TypeBase):
    id: int

    class Config:
        orm_mode = True


class PlaceBase(BaseModel):
    name: str
    city: str
    latitude: float
    longitude: float


class PlaceCreate(PlaceBase):
    types: List[str]  # nomes dos tipos (ex: "bares", "museus", etc.)


class PlaceOut(PlaceBase):
    id: int
    type: List[TypeOut]  # tipo do local

    class Config:
        orm_mode = True
