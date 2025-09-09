from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.api.database import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="schedules")
    items = relationship("ScheduleItem", back_populates="schedule", cascade="all, delete-orphan")


class ScheduleItem(Base):
    __tablename__ = "schedule_items"

    id = Column(Integer, primary_key=True, index=True)
    schedule_id = Column(Integer, ForeignKey("schedules.id", ondelete="CASCADE"))
    place_id = Column(Integer, ForeignKey("places.id"), nullable=True)  # pode ser nulo
    custom_name = Column(String, nullable=True)  # se não tiver place
    start_time = Column(String, nullable=True)  # pode ser datetime ou apenas HH:mm
    end_time = Column(String, nullable=True) 
    duration_minutes = Column(Integer, nullable=True)

    schedule = relationship("Schedule", back_populates="items")
    place = relationship("Place", back_populates="schedule_items", lazy="joined")
