path := .

.PHONY: help
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:
	pipenv install

activate:
	pipenv shell

run:
	python manage.py runserver

test:
	python manage.py test

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

up:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

rebuild:
	docker-compose build --no-cache
