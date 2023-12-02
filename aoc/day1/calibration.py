from __future__ import annotations


class CalibrationLine:
    def __init__(self, line: str, named_digit: bool = False):
        self._line: str = line
        self._digits = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        self._named_digit = named_digit

    def _first(self) -> str:
        text = ""
        for letter in self._line:
            if letter.isdigit():
                return letter
            elif self._named_digit:
                text += letter
                digit = self._check_word(text, reverse=False)
                if digit:
                    return digit
        assert False, "unreachable"

    def _last(self) -> str:
        text = ""
        for letter in self._line[::-1]:
            if letter.isdigit():
                return letter
            elif self._named_digit:
                text += letter
                digit = self._check_word(text, reverse=True)
                if digit:
                    return digit
        assert False, "unreachable"

    @property
    def calibration_value(self) -> int:
        pair = int("".join([self._first(), self._last()]))
        return pair

    def _check_word(self, word: str, reverse: bool = False) -> str:
        for key in self._digits:
            check_key = key[::-1] if reverse else key
            if check_key in word:
                return self._digits[key]
        assert False, "unreachable"
