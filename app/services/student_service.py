from sqlalchemy.orm import Session
from fastapi import HTTPException

from app import models
from app.schemas import StudentCreate
from app.utils import hash_password


def register_student(student: StudentCreate, db: Session):

    existing_student = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(student.password)

    new_student = models.Student(
        full_name=student.full_name,
        email=student.email,
        password=hashed_password,
        phone=student.phone,
        jee_percentile=student.jee_percentile,
        branch_preference=student.branch_preference
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student registered successfully",
        "student_id": new_student.id
    }