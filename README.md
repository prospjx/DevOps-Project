# Task Management API

A FastAPI-based Task Management API built as a hands-on DevOps learning project. The application uses PostgreSQL for data persistence and Docker for containerization.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions
- Pytest
- Black
- Ruff

## Features

- Create tasks
- Retrieve tasks
- Store task data in PostgreSQL
- Interactive API documentation with FastAPI/Swagger
- Automated testing with Pytest
- Code quality checks with Black and Ruff
- Automated Docker image builds through GitHub Actions

## Project Structure

```text
task-management-api/
├── .github/
│   └── workflows/
├── app/
├── docker/
├── k8s/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Running Locally

### Prerequisites

- Python
- Docker
- Git

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd task-management-api
```

### 2. Configure environment variables

Create a `.env` file based on `.env.example`.

```env
APP_NAME=Task Management API
APP_VERSION=1.0.0
ENVIRONMENT=development
DATABASE_URL=postgresql://postgres:password123@localhost:5432/tasksdb
```

> Do not commit your `.env` file to GitHub.

### 3. Start the application

```bash
docker compose -f docker/docker-compose.yml up --build
```

The API will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

## Testing

Run the test suite with:

```bash
pytest
```

## Code Quality

Check formatting with Black:

```bash
black --check .
```

Run Ruff:

```bash
ruff check .
```

## CI/CD

GitHub Actions automatically:

1. Checks code formatting with Black.
2. Runs Ruff linting.
3. Runs Pytest.
4. Builds the Docker image.
5. Pushes the image to the configured container registry.

## Current Status

🚧 The project is currently under development.

Future improvements include Kubernetes deployment, Terraform-managed infrastructure, AWS deployment, and Prometheus/Grafana monitoring.