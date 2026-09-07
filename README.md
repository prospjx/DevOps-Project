# Task Management API

A production-ready FastAPI-based Task Management API built as an end-to-end DevOps and Cloud Engineering project. The stack integrates Python API development, PostgreSQL persistence, Docker Compose orchestration, Prometheus & Grafana observability, Kubernetes deployments, and automated CI/CD pipelines.

![Architecture Diagram](architecture-diagram.svg)

---

## Overview

Key highlights of this project:

- **FastAPI REST API**: High-performance asynchronous API for task management.
- **PostgreSQL Database**: Relational data persistence with SQLAlchemy ORM.
- **Monitoring & Observability**: Integrated Prometheus metric collection (`/metrics`) and Grafana visualization.
- **Containerization**: Multi-container setup with Docker & Docker Compose.
- **Kubernetes Manifests**: Production-style manifests including Deployments, Services, ConfigMaps, Secrets, Ingress, and ServiceMonitor.
- **Infrastructure as Code (IaC)**: Cloud infrastructure provisioning defined with Terraform.
- **CI/CD Pipeline**: GitHub Actions workflows for automated linting, formatting, testing, and container registry publishing.
- **Interactive Documentation**: Auto-generated Swagger/OpenAPI interactive docs.

---

## Tech Stack

- **Backend**: Python 3.12, FastAPI, Pydantic, SQLAlchemy
- **Database**: PostgreSQL 16
- **Observability**: Prometheus, Grafana
- **Containerization & Orchestration**: Docker, Docker Compose, Kubernetes
- **Infrastructure as Code**: Terraform
- **CI/CD & Automation**: GitHub Actions, GitHub Packages / Docker Hub
- **Code Quality & Testing**: Pytest, Black, Ruff

---

## Features

- Full CRUD operations for task tracking (create, list, manage).
- Health check endpoint (`/health`) with live database ping verification.
- Metrics endpoint (`/metrics`) tracking HTTP request counts, status codes, and unhandled exceptions.
- Automated code formatting and style validation with Black and Ruff.
- Automated test execution with Pytest.
- Multi-container local development stack (FastAPI + PostgreSQL + Prometheus + Grafana).
- Declarative Kubernetes deployment manifests ready for local (Minikube / Kind) or cloud clusters.

---

## Project Structure

```text
fastapi-redis-app/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── test_main.py
│   ├── models/
│   │   └── task.py
│   ├── routes/
│   │   └── tasks.py
│   └── schemas/
├── docker/
│   ├── Dockerfile
│   ├── compose.yaml
│   └── prometheus.yaml
├── k8s/
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── postgres.yaml
│   ├── secret.yaml
│   ├── service.yaml
│   └── servicemonitor.yaml
├── .github/
│   └── workflows/
├── .env.example
├── .gitignore
├── architecture-diagram.svg
├── monitoring.md
├── main.tf
├── output.tf
├── variables.tf
├── terraform.tfvars
├── requirements.txt
└── README.md
```

---

## Running Locally with Docker Compose

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)
- [Git](https://git-scm.com/)
- Python 3.10+ (for local scripts/tests)
- [Terraform](https://www.terraform.io/) (optional, for cloud provisioning)

### 1. Clone the repository

```bash
git clone https://github.com/prospjx/DevOps-Project.git
cd DevOps-Project
```

### 2. Configure environment variables

Create a `.env` file based on [.env.example](.env.example):

```bash
cp .env.example .env
```

Default contents:

```env
APP_NAME=Task Management API
APP_VERSION=1.0.0
ENVIRONMENT=development
DATABASE_URL=postgresql://postgres:password123@postgresql:5432/tasksdb
```

> [!NOTE]
> Do not commit your personal `.env` file to version control.

### 3. Start the application stack

```bash
docker compose -f docker/compose.yaml up --build
```

This launches:
- **FastAPI**: http://localhost:8000
- **PostgreSQL**: `localhost:5432`
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000

---

## Service URLs & Endpoints

| Service / Endpoint | URL | Description |
| :--- | :--- | :--- |
| **API Root** | `http://localhost:8000/` | Application metadata and environment info |
| **Swagger UI** | `http://localhost:8000/docs` | Interactive OpenAPI documentation |
| **Health Check** | `http://localhost:8000/health` | Service and database connectivity check |
| **Metrics** | `http://localhost:8000/metrics` | Prometheus metrics endpoint |
| **Prometheus UI** | `http://localhost:9090` | Prometheus metric explorer & query console |
| **Grafana UI** | `http://localhost:3000` | Observability dashboards |

---

## API Documentation

### `GET /`
Returns service metadata loaded from environment variables.

**Response (`200 OK`):**
```json
{
  "first": "Task Management API",
  "version": "1.0.0",
  "environment": "development"
}
```

---

### `GET /health`
Validates that the API can successfully communicate with PostgreSQL.

**Response (`200 OK`):**
```json
{
  "status": "healthy",
  "database": "connected"
}
```

---

### `POST /tasks/`
Creates a new task.

**Request Body (`application/json`):**
```json
{
  "title": "Finish project proposal",
  "description": "Write the final draft before Friday",
  "due": "2026-08-20"
}
```

**Response (`200 OK`):**
```json
{
  "id": 1,
  "title": "Finish project proposal",
  "description": "Write the final draft before Friday",
  "due": "2026-08-20",
  "completed": false
}
```

---

### `GET /tasks/`
Retrieves a paginated list of tasks. Supports query parameters `skip` and `limit`.

**Response (`200 OK`):**
```json
[
  {
    "id": 1,
    "title": "Finish project proposal",
    "description": "Write the final draft before Friday",
    "due": "2026-08-20",
    "completed": false
  }
]
```

---

## Deploying to Kubernetes

Kubernetes manifests are located in [`k8s/`](k8s/):

1. **Deploy secrets and configurations:**
   ```bash
   kubectl apply -f k8s/secret.yaml
   kubectl apply -f k8s/configmap.yaml
   ```

2. **Deploy PostgreSQL and the FastAPI application:**
   ```bash
   kubectl apply -f k8s/postgres.yaml
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

3. **Deploy Ingress & Prometheus ServiceMonitor (optional):**
   ```bash
   kubectl apply -f k8s/ingress.yaml
   kubectl apply -f k8s/servicemonitor.yaml
   ```

---

## Testing & Code Quality

### Run Unit Tests
```bash
pytest
```

### Check Code Formatting
```bash
black --check .
```

### Run Linter
```bash
ruff check .
```

---

## CI/CD Pipeline

The GitHub Actions workflow automates quality gates and deployment artifacts on every push/PR:

1. **Linting & Quality**: Runs Ruff and verifies code style with Black.
2. **Testing**: Runs the Pytest test suite.
3. **Container Build**: Builds the Docker image.
4. **Registry Push**: Tags and pushes images to Docker Hub / GitHub Container Registry (GHCR).

---

## Roadmap

- [x] Containerized local environment with Docker Compose
- [x] Database persistence with PostgreSQL
- [x] Prometheus metrics & Grafana integration
- [x] Kubernetes manifests (Deployment, Services, Ingress, ServiceMonitor)
- [ ] Add Redis caching layer for read-heavy task endpoints
- [ ] Helm chart packaging for simplified Kubernetes deployment
- [ ] Automated staging deployment in CI/CD pipeline