.PHONY: tests

tests:
	pipenv run pytest tests
init:
	pipenv install
