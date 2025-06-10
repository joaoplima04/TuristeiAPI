from sqlalchemy.orm import Session
from app.api.models.user import User
from app.api.models.user import Preference
from app.api.schemas.user import UserCreate
from app.security import hash_password


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_or_create_preference(db: Session, name: str) -> Preference:
    preference = db.query(Preference).filter(Preference.name == name).first()
    if not preference:
        preference = Preference(name=name)
        db.add(preference)
        db.commit()
        db.refresh(preference)
    return preference


def create_user(db: Session, user_data: UserCreate):
    user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )

    # Adiciona as preferências (se houver)
    if user_data.preferences:
        for pref_name in user_data.preferences:
            preference = get_or_create_preference(db, pref_name)
            user.preferences.append(preference)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
