# app/routes/users.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.security import verify_password
from app.api.database import get_db
from app.api.models.user import User
from app.api.schemas.user import UserCreate, UserLogin, UserOut
from app.api.services.user_service import create_user, get_user_by_email, get_user_by_id

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/cadastro", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica se o email já está cadastrado
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/login", response_model=UserOut)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return db_user
    