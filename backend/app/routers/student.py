from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.dependencies import get_current_student, get_db
from app.schemas import (
    StudentCreate,
    StudentLogin,
    StudentProfileUpdate
)
from app.services.student_service import (
    register_student,
    login_student,
    update_profile
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


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
def get_my_profile(
    current_student: models.Student = Depends(get_current_student)
):
    return current_student


@router.put("/profile")
def update_student_profile(
    student: StudentProfileUpdate,
    current_student: models.Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    return update_profile(student, current_student, db)