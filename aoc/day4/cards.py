class Card:
    def __init__(self, line: str):
        self._line: str = line
        self._number: int = self._get_card_no()
        self._winning_numbers: set[int] = self._get_winning_numbers()
        self._drawn_numbers: set[int] = self._get_drawn_numbers()

    def _get_card_no(self) -> int:
        card_no = self._line.split(":")[0]
        number = next(num for num in iter(card_no.split()) if num.isdigit())
        return int(number)

    def _get_winning_numbers(self) -> set[int]:
        lottery = self._line.split(":")[1]
        winning_numbers = lottery.split("|")[0]
        return set([int(x) for x in winning_numbers.split() if x.isdigit()])

    def _get_drawn_numbers(self) -> set[int]:
        lottery = self._line.split(":")[1]
        drawn_numbers = lottery.split("|")[1]
        return set([int(x) for x in drawn_numbers.split() if x.isdigit()])

    @property
    def points(self) -> int:
        points = 2 ** (self.number_of_matches - 1) if self.number_of_matches else 0
        return int(points)

    @property
    def number_of_matches(self) -> int:
        number_of_matches = len(self._winning_numbers.intersection(self._drawn_numbers))
        return number_of_matches

    @property
    def number(self) -> int:
        return self._number

    def __repr__(self) -> str:
        return f"Card(number={self._number}, number_of_matches={self.number_of_matches}, _winning_numbers={self._winning_numbers}, _drawn_numbers={self._drawn_numbers})"


class CardRepository:
    def __init__(self, cards: list[Card]):
        self._cards: list[Card] = cards

    @property
    def total_won_cards(self) -> int:
        counter = {k.number: 1 for k in self._cards}
        for card in self._cards:
            for j in range(1, card.number_of_matches + 1):
                counter[card.number + j] += counter[card.number]
        return sum(counter.values())
