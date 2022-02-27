.PHONY: install format lint test sec

install:
	@poetry install
	@poetry export -f requirements.txt --output requirements.txt
format:
	@poetry run isort .
	@poetry run blue .
lint:
	@poetry run blue . --check
	@poetry run isort . --check
	@poetry run prospector --with-tool pep257 --doc-warning
test:
	@poetry run pytest -v
sec:
	@poetry run pip-audit