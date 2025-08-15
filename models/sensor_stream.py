from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class SensorStream(Base):
    __tablename__ = "sensor_streams"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient_profiles.id"), nullable=False)
    sensor_type = Column(String, nullable=False)
    payload = Column(JSON, default={})
    timestamp = Column(DateTime, default=datetime.utcnow)

    patient = relationship("PatientProfile", back_populates="sensor_streams")
