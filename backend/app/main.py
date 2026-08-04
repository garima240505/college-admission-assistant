from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import Base, engine
from app.routers import student, chatbot

# Create FastAPI app
app = FastAPI(title=settings.APP_NAME)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://college-admission-assistant-garima240505s-projects.vercel.app",
        "https://college-admission-assistant-rose.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(student.router)
app.include_router(chatbot.router)

# Home route
@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "debug": settings.DEBUG
    }