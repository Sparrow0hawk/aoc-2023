from aoc.day4.cards import Card, CardRepository

data = "data/day4.txt"

with open(data) as open_file:
    cards = [Card(line=line) for line in open_file.readlines()]

card_repo = CardRepository(cards=cards)

print(f"The solution to day 4 part 2 is {card_repo.total_won_cards}")
