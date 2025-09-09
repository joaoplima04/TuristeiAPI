from typing import List, Optional
from pydantic import BaseModel

class ScheduleItemCreate(BaseModel):
    place_id: Optional[int] = None   # se for uma atração cadastrada
    custom_name: Optional[str] = None  # se for algo customizado (ex: café da manhã)
    start_time: Optional[str] = None
    duration_minutes: Optional[int] = None

class ScheduleCreate(BaseModel):
    title: str
    user_id: int
    items: List[ScheduleItemCreate]

class ScheduleOut(BaseModel):
    id: int
    title: str
    user_id: int
    items: List[ScheduleItemCreate]

    class Config:
        orm_mode = True
