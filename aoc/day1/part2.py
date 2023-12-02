from aoc.day1.calibration import CalibrationLine

file = "data/day1.txt"

calibration_values = []

with open(file) as open_file:
    for file_line in open_file.readlines():
        calibration_line = CalibrationLine(line=file_line, named_digit=True)

        calibration_values.append(calibration_line.calibration_value)

print(f"Solution to day1 part 2 is: {sum(calibration_values)}")
