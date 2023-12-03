from aoc.day3.engine_schematic import EngineSchematic

data = "data/day3.txt"

schematic = EngineSchematic()

with open(data) as open_file:
    for line in open_file.readlines():
        schematic.add_line(line=line)

print(f"The solution to day 3 part 1 is {sum(schematic.symbol_search())}")
