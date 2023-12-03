def parse_input(file_path):
	result = []
	with open(file_path, 'r') as input_file:
		result = input_file.readlines()

	return result


test = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def get_digits(str):
	return filter(lambda x:x.isdigit(), str)

def problem1(data):
	result = 0

	for line in data:
		first = next(get_digits(line))
		last = next(get_digits(reversed(line)))
		result += int(first + last)

	return result

test = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

def problem2(data):
	pass



problem1(parse_input("input1"))
