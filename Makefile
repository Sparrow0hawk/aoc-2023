dirs = aoc tests
bin = .venv/bin

format:
	$(bin)/ruff format $(dirs)

lint: ruff-check mypy

fix:
	$(bin)/ruff check fix $(dirs)

test:
	$(bin)/pytest

ruff-check:
	$(bin)/ruff check $(dirs)

mypy:
	$(bin)/mypy $(dirs)
