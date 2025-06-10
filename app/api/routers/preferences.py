from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.database import get_db
from app.api.schemas.preference import PreferenceBase, PreferenceOut
from app.api.models.user import Preference
from typing import List

router = APIRouter(
    prefix="/preferences",
    tags=["preferences"]
)

@router.post("/", response_model=PreferenceOut)
def create_preference(preference: PreferenceBase, db: Session = Depends(get_db)):
    new_pref = Preference(**preference.dict())
    db.add(new_pref)
    db.commit()
    db.refresh(new_pref)
    return new_pref

@router.get("/get-preferences", response_model=List[PreferenceOut])
def list_preferences(db: Session = Depends(get_db)):
    return db.query(Preference).all()
