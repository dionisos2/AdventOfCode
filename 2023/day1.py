def parse_input(file_path):
	result = []
	with open(file_path, 'r') as input_file:
		result = input_file.readlines()

	return result

def get_digits(string, reverse = False):
	if reverse:
		string = reversed(string)
	return filter(lambda x:x.isdigit(), string)

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
reversed_numbers = [n[::-1] for n in numbers]

def get_spelled_digits(string, reverse = False):
	global reversed_numbers, numbers

	if reverse:
		string = string[::-1]
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
	value = lambda line: int(next(get_digits(line)) + next(get_digits(line, True)))

	return sum(value(line) for line in data)

data = parse_input("input1")

print(problem1(data))
print(problem1(data, get_spelled_digits))
