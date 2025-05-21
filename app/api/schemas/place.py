from pydantic import BaseModel
from app.enums import PlaceTypeEnum

class PlaceBase(BaseModel):
    name: str
    city: str
    latitude: float
    longitude: float
    type: PlaceTypeEnum

class PlaceCreate(PlaceBase):
    pass

class PlaceOut(PlaceBase):
    id: int

    class Config:
        orm_mode = True
