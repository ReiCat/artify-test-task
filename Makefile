# Read .env file
ifneq (,$(wildcard ./.env))
    include ./.env
    export
endif

VENV_PATH?=./venv
PYTHON=${VENV_PATH}/bin/python3

run: 
	${PYTHON} main.py
