from pydantic import BaseModel
from typing import List, Optional
from app.api.schemas.place import PlaceOut
from datetime import date

class ScheduleItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    place_id: Optional[int] = None

class ScheduleCreate(BaseModel):
    title: str
    user_id: int
    date: Optional[str] = None
    items: List[ScheduleItemCreate]

class ScheduleItemOut(BaseModel):
    id: int
    title: Optional[str] = None  # renomeado de title
    description: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    place_id: Optional[int] = None
    place: Optional[PlaceOut] = None

    class Config:
        orm_mode = True


class ScheduleOut(BaseModel):
    id: int
    title: str
    date: Optional[date]  # retorna string YYYY-MM-DD
    items: List[ScheduleItemOut] = []

    class Config:
        orm_mode = True
