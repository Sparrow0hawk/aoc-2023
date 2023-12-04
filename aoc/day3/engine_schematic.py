from __future__ import annotations
import re
from dataclasses import dataclass


class EngineSchematic:
    def __init__(self) -> None:
        self._lines: list[Line] = []
        self._part_numbers: list[int] = []
        self._SYMBOLS: set[str] = {"*", "-", "%", "=", "+", "@", "$", "#", "&", "/"}

    def add_line(self, line: str) -> None:
        self._lines.append(Line(line=line))

    def _find_on_line(self, line_no: int, index: int) -> str | None:
        if line_no <= (len(self._lines) - 1) and 0 <= index <= (
            len(self._lines[0].line) - 1
        ):
            return self._lines[line_no].line[index]
        else:
            return None

    def symbol_search(self) -> list[int]:
        part_numbers = []
        for line_no, line in enumerate(self._lines):
            for part_number in line._part_numbers:
                scanning_coords = list(
                    (x, y)
                    for x in range(part_number.start - 1, part_number.end + 1)
                    for y in range(line_no - 1, line_no + 2)
                )
                for x, y in scanning_coords:
                    if self._find_on_line(index=x, line_no=y) in self._SYMBOLS:
                        part_numbers.append(int(part_number.value))
        return part_numbers

    @property
    def part_numbers(self) -> list[list[PartNumber]]:
        return [line._part_numbers for line in self._lines]


@dataclass
class PartNumber:
    start: int
    end: int
    value: str


class Line:
    def __init__(self, line: str):
        self._line: str = line
        self._part_numbers: list[PartNumber] = self.find_part_numbers()

    def find_part_numbers(self) -> list[PartNumber]:
        number_search = re.finditer(r"\d+", self._line)
        return [
            PartNumber(start=match.span()[0], end=match.span()[1], value=match.group())
            for match in number_search
            if number_search
        ]

    @property
    def line(self) -> str:
        return self._line
