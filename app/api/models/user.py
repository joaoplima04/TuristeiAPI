from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum as SqlEnum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.api.database import Base
from app.enums import PreferenceType

# Tabela de associação entre usuários e preferências salvas no cadastro
user_preferences = Table(
    "user_preferences",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("preference_id", Integer, ForeignKey("preferences.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relacionamento muitos-para-muitos com preferências
    preferences = relationship("Preference", back_populates="user", cascade="all, delete")