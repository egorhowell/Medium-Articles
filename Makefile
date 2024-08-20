SHELL=/bin/bash

PHONY: install
install:
	poetry install

PHONY: format
format:
	poetry run black .
	poetry run isort .

PHONY: lint
lint:
	poetry run black . --check
	poetry run isort . --check-only
