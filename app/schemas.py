from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str
    jee_percentile: float
    branch_preference: str


class StudentLogin(BaseModel):
    email: EmailStr
    password: str


class StudentProfileUpdate(BaseModel):
    category: str
    state: str
    twelfth_percentage: float


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str