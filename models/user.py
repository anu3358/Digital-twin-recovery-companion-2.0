from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # patient, clinician, admin
    full_name = Column(String)
    is_active = Column(Boolean, default=True)

    patient_profile = relationship("PatientProfile", back_populates="user", uselist=False)
    audit_logs = relationship("AuditLog", back_populates="user", cascade="all, delete-orphan")
