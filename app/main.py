from fastapi import FastAPI
from app.config import settings
from app.models.task import Task
from app.database import engine, Base
from app.routes.tasks import router as tasks_router

# Creates the tables in your database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registers the database tasks router
app.include_router(tasks_router)

@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    }
