install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

package-install:
	uv tool uninstall hexlet-code
	uv tool install dist/*.whl

lint:
	uv run ruff check