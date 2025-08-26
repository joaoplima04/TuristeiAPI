from sqlalchemy.orm import Session
from app.api.models.place import Place
from app.api.schemas.place import PlaceCreate
from app.api.models.user import Preference

def create_place(db: Session, place_data: PlaceCreate):
    place = Place(
        name=place_data.name,
        city=place_data.city,
        latitude=place_data.latitude,
        longitude=place_data.longitude,
        description=place_data.description,
        image_url=place_data.image_url
    )

    # Buscar ou criar preferências
    preferences = db.query(Preference).filter(Preference.name.in_(place_data.preferences)).all()
    place.preferences = preferences

    db.add(place)
    db.commit()
    db.refresh(place)
    return place

def get_place_by_id(db: Session, place_id: int) -> Place | None:
    return db.query(Place).filter(Place.id == place_id).first()
