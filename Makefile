dirs = "aoc"

format:
	ruff format $(dirs)

lint:
	ruff check $(dirs)

fix:
	ruff check fix $(dirs)

test:
	pytest
