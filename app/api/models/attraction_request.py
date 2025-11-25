from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.api.database import Base

class AttractionRequest(Base):
    __tablename__ = "attraction_requests"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    description = Column(String)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="attraction_requests")

    status = Column(String, default="pendente")
