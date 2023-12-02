dirs = "aoc"
bin = ".venv/bin"

format:
	$(bin)/ruff format $(dirs)

lint:
	$(bin)/ruff check $(dirs)

fix:
	$(bin)/ruff check fix $(dirs)

test:
	$(bin)/pytest
