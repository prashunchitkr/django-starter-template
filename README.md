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
- **Dockerfile** with multi-stage build, gunicorn, production-ready
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
│   ├── settings/       # Modular settings (one file per concern)
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
│   └── models/         # UUIDPrimaryKey, Timestamps, BaseModel
├── Dockerfile          # Multi-stage production build
├── docker-compose.yml  # PostgreSQL + Valkey + Web
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

## Environments

| Setting Class | Environment | Use Case |
|---------------|-------------|----------|
| `DevelopmentSettings` | `development` | Local development |
| `TestingSettings` | `testing` | Automated tests |
| `StagingSettings` | `staging` | Pre-production |
| `ProductionSettings` | `production` | Production deployment |

Set `DJANGO_CONFIGURATION` to switch between environments.

## Deployment

```bash
# Build and push Docker image
docker build -t myapp:latest .

# Run with production settings
docker run -e DJANGO_CONFIGURATION=ProductionSettings myapp:latest
```

Or using Docker Compose for production:

```bash
DJANGO_CONFIGURATION=ProductionSettings docker compose up web
```
