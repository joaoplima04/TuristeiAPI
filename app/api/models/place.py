from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.api.database import Base

# Tabela de associação entre usuários e preferências salvas no cadastro
place_type = Table(
    "place_type",
    Base.metadata,
    Column("place_id", Integer, ForeignKey("places.id"), primary_key=True),
    Column("type_id", Integer, ForeignKey("type.id"), primary_key=True),
)

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Relacionamento muitos-para-muitos com preferências
    type = relationship(
        "Type",
        secondary=place_type,
        backref="place"
    )


class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    
    users = relationship("Place", secondary=place_type, back_populates="type")