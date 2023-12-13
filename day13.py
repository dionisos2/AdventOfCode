def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		result = []
		pattern = []
		for line in input_file.readlines():
			if line.strip() == "":
				result.append(pattern)
				pattern = []
			else:
				pattern.append(line.strip())
	result.append(pattern)
	return result

def pp(matrix):
	for line in matrix:
		print(line)

def is_reflexion(pattern, index):
	for line1, line2 in zip(pattern[index+1:], pattern[index::-1]):
		if line1 != line2:
			return False
	return True

def distance(line1, line2):

	return sum(c1!=c2 for c1, c2 in zip(line1, line2))

def is_fixed_reflexion(pattern, index):
	error = sum(distance(line1, line2) for line1, line2 in zip(pattern[index+1:], pattern[index::-1]))
	return error == 1

def find_reflexion_value(pattern, is_r):
	for index, _ in enumerate(pattern[:-1]):
		if is_r(pattern, index):
			return index+1
	return 0

def day13(patterns, is_r = is_reflexion):
	result = 0

	for pattern in patterns:
		result += 100*find_reflexion_value(pattern, is_r)
		result += find_reflexion_value(list(zip(*pattern)), is_r)
	return result

def day13_2(patterns):
	return day13(patterns, is_fixed_reflexion)

patterns = parse_input("input13")

print(day13_2(patterns))
