from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.api.database import Base

class Preference(Base):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    user = relationship("User", back_populates="preferences")