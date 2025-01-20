install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov

package-install:
	uv tool uninstall hexlet-code
	uv tool install dist/*.whl

make lint:
	uv run ruff check