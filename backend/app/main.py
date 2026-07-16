from fastapi import FastAPI
from app.config import settings
from app.routers import student, chatbot
from app.database import engine, Base
from app import models
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI application first
app = FastAPI(title=settings.APP_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(student.router)
app.include_router(chatbot.router)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "debug": settings.DEBUG
    }