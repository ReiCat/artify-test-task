# Read .env file
ifneq (,$(wildcard ./.env))
    include ./.env
    export
endif

VENV_PATH?=./venv
PYTHON=${VENV_PATH}/bin/python3

run: 
	${PYTHON} main.py

migration:
	@python manage.py script $(name)

migrate-up: 
	@python manage.py upgrade

migrate-down:
	@python manage.py downgrade $(id)