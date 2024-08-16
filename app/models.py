from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base


class User(Base):
    __tablename__ = "users"

    pk = Column(Integer, primary_key=True, index=True)
    id = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    gender = Column(String(1), nullable=False)
    birth_year = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())