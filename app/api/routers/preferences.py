from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.database import get_db
from schemas.preference import PreferenceCreate, PreferenceOut
from app.api.models.user import User
from app.api.models.preference import Preference

router = APIRouter(
    prefix="/preferences",
    tags=["preferences"]
)

@router.post("/preferences/", response_model=PreferenceOut)
def create_preference(preference: PreferenceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_pref = Preference(**preference.dict(), user_id=current_user.id)
    db.add(new_pref)
    db.commit()
    db.refresh(new_pref)
    return new_pref
