def parse_input(file_path):
	result = []
	with open(file_path, 'r') as input_file:
		result = input_file.readlines()

	return result


test1 = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
test2 = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

def get_digits(str, reverse = False):
	return filter(lambda x:x.isdigit(), str)

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
reversed_numbers = [n[::-1] for n in numbers]

def get_spelled_digits(string, reverse = False):
	global reversed_numbers, numbers

	if reverse:
		nums = reversed_numbers
	else:
		nums = numbers

	for i, l in enumerate(string):

		if l.isdigit():
			yield l

		for j in range(3,6):
			try:
				yield str(nums.index(string[i:i+j]))
			except ValueError:
				continue

def problem1(data, get_digits = get_digits):
	result = 0

	for line in data:
		first = next(get_digits(line))
		last = next(get_digits(line[::-1], True))
		result += int(first + last)

	return result

data = parse_input("input1")
# problem1(data)
problem1(data, get_spelled_digits)


