from fastapi import HTTPException
from fastapi import FastAPI
from app.config import settings

app = FastAPI()

items = ["Docker", "Container", "Kubernetes", "Prometheus", "Redis"]

@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
}

@app.get("/again")
def again():
    return {"message": "This again"}

@app.get("/items/{item_id}")
def show_items(item_id: int):
    if item_id < len(items):
        return {"items": items[item_id], "id": item_id}
    else: 
        raise HTTPException(status_code=404, detail="Item not Found")

