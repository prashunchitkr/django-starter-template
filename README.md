# Django Starter Template

A modern Django REST Framework starter template with JWT authentication, Docker, and CI/CD.

## Features

- **Python 3.14+** with `uv` package manager
- **Django REST Framework** with JWT auth (SimpleJWT)
- **django-configurations** — class-based settings with environment-driven config
- **Custom User model** — email-based authentication (no username), UUID primary keys
- **PostgreSQL 18** + **Valkey 8** (Redis fork) via Docker Compose
- **OpenAPI docs** via drf-spectacular (Swagger UI, dev-only)
- **Health check endpoints** for container orchestration
- **ASGI** — uvicorn for async deployment
- **Celery** — async task queue with valkey broker
- **Structured logging** — structlog with colored dev console, JSON for production, daily log rotation
- **Dockerfile** with multi-stage build, uvicorn, production-ready
- **CI/CD** via GitHub Actions (lint, typecheck, test, Docker build)
- **Testing** with pytest, pytest-django, factory-boy, coverage
- **Linting** with Ruff + **Type checking** with mypy + django-stubs
- **Pre-commit hooks** for automated quality checks

## Quick Start

```bash
# Clone and enter the project
git clone <repo-url> && cd django-starter-template

# Copy environment file
cp env.example .env

# Install dependencies
make install

# Run migrations
make migrate

# Start the dev server
make run
```

### With Docker

```bash
docker compose up --build
```

## Project Structure

```
├── core/               # Django project package
│   ├── asgi.py         # ASGI entrypoint (uvicorn)
│   ├── celery.py       # Celery app
│   ├── settings/       # Modular settings (one file per concern)
│   │   ├── _logging.py    # structlog config, console renderer, rotation
│   │   └── ...
│   ├── middlewares/
│   │   └── logging.py     # RequestLoggingMiddleware
│   └── urls.py         # Root URL configuration
├── _auth/              # Custom user authentication app
│   ├── models/         # User model (email-based, UUID PK)
│   ├── serializers/    # JWT token + user serializers
│   ├── views/          # API views
│   └── urls/           # Auth URL routing
├── health/             # Health check endpoints
│   ├── views/          # Public + authenticated health checks
│   └── serializers/    # Response serializers
├── base/               # Base model mixins
│   ├── mixins/
│   │   └── logger.py   # LoggingMixin for DRF views
│   └── models/         # UUIDPrimaryKey, Timestamps, BaseModel
├── Dockerfile          # Multi-stage production build (uvicorn CMD)
├── docker-compose.yml  # PostgreSQL + Valkey + Web + Celery worker
└── Makefile            # Common commands
```

## Available Commands

| Command | Description |
|---------|-------------|
| `make install` | Install dependencies |
| `make migrate` | Run database migrations |
| `make test` | Run tests with coverage |
| `make lint` | Run Ruff + mypy |
| `make format` | Format code with Ruff |
| `make run` | Start development server |
| `make shell` | Django shell |
| `make superuser` | Create superuser |
| `make celery` | Run Celery worker |

## Environments

| Setting Class | Environment | Use Case |
|---------------|-------------|----------|
| `DevelopmentSettings` | `development` | Local development |
| `TestingSettings` | `testing` | Automated tests |
| `StagingSettings` | `staging` | Pre-production |
| `ProductionSettings` | `production` | Production deployment |

Set `DJANGO_CONFIGURATION` to switch between environments.

## Logging

All logs use **structlog** via `ProcessorFormatter`, ensuring consistent output across Django, DRF, uvicorn, and Celery.

### Development

```text
2026-05-09T12:33:00Z [info     ] [base.mixins] [ListUserView] view method=GET path=/auth/user/list/ status_code=200 duration_ms=31.48 request_id=abc...
```

Columns: timestamp → level → logger → component name (via `subject` key) → event → key=value pairs.

- `RequestLoggingMiddleware` binds `request_id`, `method`, `path` per request.
- `LoggingMixin` on DRF views logs structured events with timing, status, and user info.

### Production

```json
{"event": "Started server process [1]", "logger": "uvicorn.error", "level": "info", "timestamp": "..."}
```

Output to **stdout** and **file** (`logs/app.log` by default). Log rotation:
- Daily rotation at midnight (`TimedRotatingFileHandler`)
- 30 backups retained
- Path configurable via `LOG_DIR` env var

## Deployment

```bash
# Build and push Docker image
docker build -t myapp:latest .

# Run with production settings (container runs uvicorn internally)
docker run -e DJANGO_CONFIGURATION=ProductionSettings myapp:latest
```

Or using Docker Compose for production:

```bash
DJANGO_CONFIGURATION=ProductionSettings docker compose up web
```
