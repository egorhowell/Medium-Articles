SHELL=/bin/bash

PHONY: install
install:
	poetry install

PHONY: lint
lint:
	poetry run black .
	poetry run isort .
