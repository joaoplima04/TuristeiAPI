# services/user_service.py
from sqlalchemy.orm import Session
from app.api.models.user import User
from app.api.models.user import Preference
from app.api.schemas.user import UserCreate
from app.security import hash_password  # Crie uma função para isso

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user_data: UserCreate):
    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        current_preferences=user_data.current_preferences  
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user