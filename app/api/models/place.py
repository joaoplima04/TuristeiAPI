from sqlalchemy import Column, Integer, String, Float, Enum as SqlEnum
from app.api.database import Base
from app.enums import PlaceTypeEnum

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    type = Column(SqlEnum(PlaceTypeEnum), nullable=False)