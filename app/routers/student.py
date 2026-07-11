from fastapi import APIRouter
from app.schemas import StudentCreate
from app.services.student_service import register_student

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/register")
def register(student: StudentCreate):
    return register_student(student)