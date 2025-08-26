from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.api.database import Base
from app.api.models.user import place_type

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    description = Column(String, nullable=True)    # texto descritivo do lugar
    image_url = Column(String, nullable=True)      # url da imagem (pode ser local ou externa)

    # Relacionamento muitos-para-muitos com preferências
    preferences = relationship(
        "Preference",
        secondary=place_type,
        back_populates="places"
    )