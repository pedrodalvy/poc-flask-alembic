up:
	docker compose up -d --build

down:
	docker compose down --remove-orphans

logs:
	docker compose logs -f app

revision:
	poetry run alembic revision -m "$(name)"

migrate:
	docker compose exec app python -m poetry run alembic upgrade head

history:
	poetry run alembic history

downgrade:
	docker compose exec app python -m poetry run alembic downgrade "$(revision)"

.PHONY: up down logs revision migrate history downgrade
