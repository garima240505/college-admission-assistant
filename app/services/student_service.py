from sqlalchemy.orm import Session
from fastapi import HTTPException

from app import models
from app.schemas import StudentCreate, StudentLogin
from app.utils import hash_password, verify_password
from app.auth import create_access_token


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


def login_student(student: StudentLogin, db: Session):

    existing_student = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if not existing_student:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        student.password,
        existing_student.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": existing_student.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


def update_profile(student_data, current_student, db: Session):

    student = db.query(models.Student).filter(
        models.Student.id == current_student.id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.category = student_data.category
    student.state = student_data.state
    student.twelfth_percentage = student_data.twelfth_percentage

    db.commit()
    db.refresh(student)

    return {
        "message": "Profile updated successfully"
    }