from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    phone = Column(String(20), nullable=False)

    jee_percentile = Column(Float, nullable=False)

    branch_preference = Column(String(100), nullable=False)