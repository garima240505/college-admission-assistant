from fastapi import FastAPI
from app.config import settings
from app.routers import student
from app.database import engine, Base
from app import models

# Create the FastAPI application first
app = FastAPI(title=settings.APP_NAME)
Base.metadata.create_all(bind=engine)
# Then register the router
app.include_router(student.router)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "debug": settings.DEBUG
    }