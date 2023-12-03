import pytest

from aoc.day3.engine_schematic import Line, EngineSchematic


@pytest.fixture
def part1_test() -> str:
    return """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_engine_schematic(part1_test: str) -> None:
    schematic = EngineSchematic()
    for line in part1_test.splitlines():
        schematic.add_line(line=line)

    assert sum(schematic.symbol_search()) == 4361
