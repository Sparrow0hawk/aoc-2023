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
        number_of_matches = self.number_of_winners
        return 2 ** (number_of_matches - 1) if number_of_matches else 0

    @property
    def number_of_winners(self) -> int:
        number_of_matches = len(self._winning_numbers.intersection(self._drawn_numbers))
        return number_of_matches

    def __repr__(self):
        return f"Card(number={self._number}, number_of_winners={self.number_of_winners}, _winning_numbers={self._winning_numbers}, _drawn_numbers={self._drawn_numbers})"
