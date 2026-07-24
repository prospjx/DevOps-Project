from fastapi import FastAPI
from redis_client import set_value, get_value

app = FastAPI()

@app.get("/set")
def set_data(key: str, value: str):
    """Store a key/value pair in Redis."""
    success = set_value(key, value)
    return {"status": "ok" if success else "error"}

@app.get("/get")
def get_data(key: str):
    """Retrieve a value from Redis."""
    value = get_value(key)
    return {"value": value}
