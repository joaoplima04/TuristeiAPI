from sqlalchemy.orm import Session
from app.api.models.user import User
from app.api.models.place import Place
from app.api.models.user import Preference

def get_recommendations(db: Session, user_id: int):
    # Busca o usuário e suas preferências
    user = db.query(User).filter(User.id == user_id).first()

    if not user or not user.preferences:
        return []

    # Extrai os nomes das preferências do usuário
    preference_names = [pref.name for pref in user.preferences]

    # Busca os lugares com preferências que correspondem às do usuário
    places = (
        db.query(Place)
        .join(Place.preferences)  # relacionamento many-to-many
        .filter(Preference.name.in_(preference_names))
        .distinct()
        .all()
    )

    return places
