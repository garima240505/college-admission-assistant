from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import StudentCreate, StudentLogin
from app.services.student_service import (
    register_student,
    login_student
)
from app.database import SessionLocal
from app.dependencies import get_current_student
from app import models

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return register_student(student, db)


@router.post("/login")
def login(
    student: StudentLogin,
    db: Session = Depends(get_db)
):
    return login_student(student, db)


@router.get("/me")
def get_profile(
    current_student: models.Student = Depends(get_current_student)
):
    return {
        "id": current_student.id,
        "full_name": current_student.full_name,
        "email": current_student.email,
        "phone": current_student.phone,
        "jee_percentile": current_student.jee_percentile,
        "branch_preference": current_student.branch_preference
    }