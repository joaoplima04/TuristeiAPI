from sqlalchemy.orm import Session
from app.api.models.place import Place
from app.api.schemas.place import PlaceCreate

def create_place(db: Session, place_data: PlaceCreate) -> Place:
    place = Place(**place_data.dict())
    db.add(place)
    db.commit()
    db.refresh(place)
    return place

def get_place_by_id(db: Session, place_id: int) -> Place | None:
    return db.query(Place).filter(Place.id == place_id).first()
