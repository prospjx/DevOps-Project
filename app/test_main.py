import pytest
from fastapi.testclient import TestClient

from app.config import settings
from app.database import Base, SessionLocal, engine
from app.main import app
from app.models.task import Task

Base.metadata.create_all(bind=engine)
client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_tasks():
    with SessionLocal() as db:
        db.query(Task).delete()
        db.commit()
    yield


def task_payload(title="Finish project proposal"):
    return {
        "title": title,
        "description": "Write the final draft before Friday",
        "due": "2026-12-01",
    }


def create_task(title="Finish project proposal"):
    response = client.post("/tasks/", json=task_payload(title))
    assert response.status_code == 201
    return response.json()


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "first": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "database": "connected"}


def test_create_and_read_task():
    created = create_task()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json() == {
        "id": created["id"],
        **task_payload(),
        "completed": False,
    }


def test_list_tasks_supports_pagination():
    create_task()
    create_task("Plan team meeting")

    response = client.get("/tasks/?skip=1&limit=1")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Plan team meeting"


def test_update_task_can_mark_it_completed():
    created = create_task()
    payload = {
        "title": "Finish the updated proposal",
        "description": None,
        "due": "2026-12-15",
        "completed": True,
    }

    response = client.put(f"/tasks/{created['id']}", json=payload)

    assert response.status_code == 200
    assert response.json() == {"id": created["id"], **payload}


def test_delete_task():
    created = create_task()

    response = client.delete(f"/tasks/{created['id']}")

    assert response.status_code == 204
    assert client.get(f"/tasks/{created['id']}").status_code == 404


@pytest.mark.parametrize(
    ("method", "path", "payload"),
    [
        ("get", "/tasks/999999", None),
        ("put", "/tasks/999999", task_payload()),
        ("delete", "/tasks/999999", None),
    ],
)
def test_missing_task_returns_not_found(method, path, payload):
    response = getattr(client, method)(path, json=payload) if payload else getattr(
        client, method
    )(path)

    assert response.status_code == 404


def test_invalid_task_is_rejected():
    response = client.post(
        "/tasks/",
        json={"title": "", "description": "invalid", "due": "not-a-date"},
    )

    assert response.status_code == 422


@pytest.mark.parametrize(
    ("query", "detail"),
    [
        ("skip=-1", "skip must be non-negative"),
        ("limit=0", "limit must be between 1 and 100"),
        ("limit=101", "limit must be between 1 and 100"),
    ],
)
def test_invalid_pagination_is_rejected(query, detail):
    response = client.get(f"/tasks/?{query}")

    assert response.status_code == 400
    assert response.json()["detail"] == detail
