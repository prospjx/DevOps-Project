import os
from dotenv import load_dotenv
from fastapi import FastAPI, Response, status
from sqlalchemy import text
from app.config import settings
from app.database import engine, Base
from app.routes.tasks import router as tasks_router

load_dotenv()

# Creates the tables in your database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registers the database tasks router
app.include_router(tasks_router)


@app.get("/")
def root():
    applica = os.getenv("APP_NAME")
    versio = os.getenv("APP_VERSION")
    envir = os.getenv("ENVIRONMENT")
    return {"first": applica, "version": versio, "environment": envir}


@app.get("/health")
def get_health():
    try:
        # Open a database connection connection to verify health
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, content=str(e))
