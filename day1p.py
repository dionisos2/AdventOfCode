def parse_input(file_path):
	result = []
	with open(file_path, 'r') as input_file:
		result = input_file.readlines()

	return result

def find(predicat, line, reverse=False):
	if reverse:
		line = line[::-1]

	for start in range(len(line)):
		for end in range(start+1, len(line)+1):
			part = line[start:end]
			if reverse:
				part = part[::-1]
			if predicat(part):
				return part
			if predicat(part) == None:
				break

	raise ValueError("humhum")

def digit_number(string):
	if string.isdigit():
		return True
	else:
		return None

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def digit_spelled(string):
	if string in numbers or string.isdigit():
		return True
	elif len(string) >= 5:
		return None
	else:
		return False

def transform(string):
	if string.isdigit():
		return string
	else:
		return str(numbers.index(string))

def get_value(line, predicat, transform):
	return int(transform(find(predicat, line)) + transform(find(predicat, line, True)))

def problem1(data, predicat, transform=lambda x:x):
	return sum(get_value(line, predicat, transform) for line in data)

data = parse_input("input1")
print(problem1(data, digit_spelled, transform))


