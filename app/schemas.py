from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str
    jee_percentile: float
    branch_preference: str