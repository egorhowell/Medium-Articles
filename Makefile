SHELL=/bin/bash

PHONY: lint
lint:
	poetry run black .
	poetry run isort .

