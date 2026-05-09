.PHONY: install migrate makemigrations test lint format shell run superuser

install:
	uv sync

migrate:
	uv run python manage.py migrate

makemigrations:
	uv run python manage.py makemigrations

test:
	DJANGO_CONFIGURATION=TestingSettings uv run pytest --cov --cov-report=term-missing

test-ci:
	DJANGO_CONFIGURATION=TestingSettings uv run pytest --cov --cov-report=xml --cov-report=term-missing -v

lint:
	uv run ruff check .
	uv run mypy .

format:
	uv run ruff format .

shell:
	uv run python manage.py shell

run:
	uv run python manage.py runserver

superuser:
	uv run python manage.py createsuperuser
