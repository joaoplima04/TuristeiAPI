from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.database import get_db
from app.api.schemas.preference import PreferenceBase, PreferenceOut
from app.api.models.user import Preference, User, user_preferences
from typing import List
from app.api.schemas.preference import SaveUserPreferences

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


@router.get("/get-user-preferences", response_model=List[PreferenceOut])
def get_user_preferences(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user.preferences


@router.post("/save-preferences")
def save_user_preferences(data: SaveUserPreferences, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Buscar preferências existentes com base nos nomes
    preferences = db.query(Preference).filter(Preference.name.in_(data.preferences)).all()

    # Substituir preferências atuais
    user.preferences = preferences

    db.commit()
    return {"message": "Preferências salvas com sucesso"}