import pytest

from aoc.day2.cubes import CubeBag


@pytest.fixture
def part1_cubes() -> str:
    return """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_cubes(part1_cubes: str) -> None:
    cube_bag = CubeBag(red=12, green=13, blue=14)

    for line in part1_cubes.splitlines():
        print(line)
        cube_bag.add_play(play=line)

    cube_bag.filter_plays()

    assert sum(cube_bag.valid_game_ids) == 8

def test_cubes_power(part1_cubes: str) -> None:
    cube_bag = CubeBag(red=12, green=13, blue=14)

    for line in part1_cubes.splitlines():
        print(line)
        cube_bag.add_play(play=line)

    assert sum(cube_bag.games_power) == 2286

