import pytest

from aoc.day4.cards import Card, CardRepository


@pytest.fixture
def part1() -> str:
    return """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def test_card(part1: str) -> None:
    cards = [Card(line=line) for line in part1.splitlines(keepends=True)]

    assert sum([card.points for card in cards]) == 13


def test_cards_win_more_cards(part1: str) -> None:
    cards = [Card(line=line) for line in part1.splitlines(keepends=True)]

    card_repo = CardRepository(cards=cards)

    assert card_repo.total_won_cards == 30
