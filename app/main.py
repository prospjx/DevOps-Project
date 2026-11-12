from fastapi import FastAPI, Request, Response, status
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.config import settings
from app.database import Base, engine
from app.routes.tasks import router as tasks_router

# Creates the tables in your database
Base.metadata.create_all(bind=engine)

# Define metrics
REQUEST_COUNT = Counter(
    "app_requests_total", "Total number of requests", ["method", "endpoint"]
)
EXCEPTIONS = Counter(
    "app_exceptions_total",
    "Total number of unhandled exceptions",
    ["endpoint", "exception_type"],
)

app = FastAPI()


# Middleware to count requests
@app.middleware("http")
async def count_requests(request: Request, call_next):
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    response = await call_next(request)
    return response


# Global exception handler to catch all unhandled errors and increment the counter
@app.exception_handler(Exception)
async def catch_all(request: Request, exc: Exception):
    EXCEPTIONS.labels(
        endpoint=request.url.path, exception_type=type(exc).__name__
    ).inc()
    # Return a generic 500 error response to the client
    return Response(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content="Internal Server Error",
    )


# Registers the database tasks router
app.include_router(tasks_router)


@app.get("/")
def root():
    return {
        "first": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }


@app.get("/health")
def get_health():
    try:
        # Open a database connection to verify health
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except SQLAlchemyError as e:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, content=str(e))


@app.get("/crash")
def crash():
    raise KeyError("This is a test crash")


@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
