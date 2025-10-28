from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.api.database import Base

# Tabela associativa
user_preferences = Table(
    'user_preferences',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('preference_id', ForeignKey('preferences.id'), primary_key=True)
)

# Tabela associativa entre lugares e preferências
place_type = Table(
    'place_type',
    Base.metadata,
    Column('place_id', ForeignKey('places.id'), primary_key=True),
    Column('preference_id', ForeignKey('preferences.id'), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relacionamento muitos-para-muitos
    preferences = relationship(
        "Preference",
        secondary=user_preferences,  # <- Tabela associativa
        back_populates="users",
        cascade="all, delete"
    )
        # Relacionamento com schedules
    schedules = relationship("Schedule", back_populates="user")

class Preference(Base):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # back_populates com nome correto
    users = relationship(
        "User",
        secondary=user_preferences,
        back_populates="preferences"
    )
    places = relationship("Place", secondary=place_type, back_populates="preferences")
