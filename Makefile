.PHONY: install pexport run pinstall pformat plint ptest psec

install:
	@pip install -r requirements.txt
pexport:
	@poetry export --without-hashes -f requirements.txt --output requirements.txt
pinstall:
	@poetry install
	@poetry export -f requirements.txt --output requirements.txt
pformat:
	@poetry run isort .
	@poetry run blue .
plint:
	@poetry run blue . --check
	@poetry run isort . --check
	@poetry run prospector --with-tool pep257 --doc-warning
ptest:
	@poetry run pytest -v
run:
	@cd src && python cli.py --clear --force_save_bd >> log.log
	@cd ..
psec:
	@poetry run pip-audit