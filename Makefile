install:
	uv sync

run:
	uv run gendiff

check:
    uv check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

package-install:
	uv tool uninstall hexlet-code
	uv tool install dist/*.whl

lint:
	uv run ruff check