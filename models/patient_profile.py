from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class PatientProfile(Base):
    __tablename__ = "patient_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    demographics = Column(JSON, default={})
    medical_history = Column(String)

    user = relationship("User", back_populates="patient_profile")
    sensor_streams = relationship("SensorStream", back_populates="patient", cascade="all, delete-orphan")
