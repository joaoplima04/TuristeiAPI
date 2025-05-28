from pydantic import BaseModel

class PreferenceCreate(BaseModel):
    categoria: str

class PreferenceOut(BaseModel):
    id: int
    categoria: str

    class Config:
        orm_mode = True
