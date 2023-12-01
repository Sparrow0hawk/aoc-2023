
file = "data/day1.txt"

cal_values = []

with open(file) as open_file:
    for file_line in open_file.readlines():
        num = [number for number in file_line if number.isdigit()]
        if len(num) > 1:
            calibration_value = ''.join([num[0], num[-1]])
        else:
            calibration_value = ''.join(num * 2)

        cal_values.append(int(calibration_value))

print(f"Solution to day1 part 1 is: {sum(cal_values)}")
