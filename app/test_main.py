from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["first"] == "Task Awesome"
    assert data["version"] == "3.0.0"
    assert data["environment"] == "developmentisago!"


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["database"] == "connected"


def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "title": "Hand bag",
            "description": "This is my handbag",
            "due": "03-04-2026",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Hand bag"
    assert data["description"] == "This is my handbag"
    assert data["due"] == "03-04-2026"


def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
