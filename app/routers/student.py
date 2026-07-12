from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import StudentCreate
from app.services.student_service import register_student
from app.database import SessionLocal

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