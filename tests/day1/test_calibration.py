from aoc.day1.calibration import CalibrationLine
import pytest

@pytest.fixture
def part1() -> str:
    return """1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet"""

@pytest.fixture
def part2() -> str:
    return """two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen"""


def test_calibration_part1(part1: str) -> None:
    container = []
    for line in part1.splitlines():
        calibration_line = CalibrationLine(line=line, named_digit=False)
        container.append(calibration_line.calibration_value)

    assert sum(container) == 142


def test_calibration_part2(part2: str) -> None:
    container = []
    for line in part2.splitlines():
        calibration_line = CalibrationLine(line=line, named_digit=True)
        container.append(calibration_line.calibration_value)

    assert sum(container) == 281
