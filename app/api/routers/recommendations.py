from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.api.database import get_db
from app.api.services.recommendation_service import get_recommendations
from app.api.schemas.place import PlaceOut
from typing import List

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"]
)

@router.get("/get-recommendations/{user_id}", response_model=List[PlaceOut])
def recommend_places(user_id: int, db: Session = Depends(get_db)):
    places = get_recommendations(db, user_id)

    if not places:
        raise HTTPException(status_code=404, detail="Nenhuma recomendação encontrada para este usuário.")

    return places