path := .

.PHONY: help
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:
	pipenv install

activate:
	pipenv shell

bash:
	docker exec -it reservation_web_container bash

test:
	docker exec -it reservation_web_container python manage.py test

migration:
	docker exec -it reservation_web_container python manage.py makemigrations

migrate:
	docker exec -it reservation_web_container python manage.py migrate

superuser:
	python manage.py createsuperuser

up:
	docker compose up -d

down:
	docker compose down

rebuild:
	docker compose build --no-cache
