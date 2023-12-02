from aoc.day2.cubes import CubeBag

data = "data/day2.txt"

cube_game = CubeBag(red=12, green=13, blue=14)

with open(data) as open_file:
    for line in open_file.readlines():
        cube_game.add_play(play=line)

print(f"Solution to day 2 part 1 is {sum(cube_game.games_power)}")
