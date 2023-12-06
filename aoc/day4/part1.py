from aoc.day4.cards import Card

data = "data/day4.txt"

with open(data) as open_file:
    cards = [Card(line=line) for line in open_file.readlines()]

print(f"The solution to day 4 part 1 is {sum([card.points for card in cards])}")
