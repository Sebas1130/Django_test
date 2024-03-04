# Makefile


run:
	export COMPOSE_FILE=local.yml; docker-compose up

build:
	export COMPOSE_FILE=local.yml; docker-compose build

down:
	export COMPOSE_FILE=local.yml; docker-compose down

django-shell:
		export COMPOSE_FILE=local.yml; docker-compose run --rm django python manage.py shell

container-shell:
	export COMPOSE_FILE=local.yml; docker-compose run --rm django sh