from sqlalchemy.orm import Session

from app import models
from app.schemas import StudentCreate


def register_student(db: Session, student: StudentCreate):
    new_student = models.Student(
        full_name=student.full_name,
        email=student.email,
        password=student.password
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student