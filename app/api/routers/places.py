from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.database import get_db
from app.api.schemas.place import PlaceCreate, PlaceOut
from app.api.services.place_service import create_place, get_place_by_id
from app.api.models.place import Place

router = APIRouter(
    prefix="/places",
    tags=["places"]
)

@router.post("/", response_model=PlaceOut)
def register_place(place: PlaceCreate, db: Session = Depends(get_db)):
    return create_place(db, place)

@router.get("/", response_model=list[PlaceOut])
def list_places(db: Session = Depends(get_db)):
    return db.query(Place).all()

@router.get("/{place_id}", response_model=PlaceOut)
def read_place(place_id: int, db: Session = Depends(get_db)):
    db_place = get_place_by_id(db, place_id)
    if not db_place:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_place