class Number:
	def __init__(self, value, row, start, end):
		self.value = value
		self.row = row
		self.start = start
		self.end = end

def parse_input(file_path):
	matrix = []
	numbers = []

	with open(file_path, 'r') as input_file:
		for row, line in enumerate(input_file.readlines()):
			matrix.append(line)
			number_start = 0
			read_number = False
			value = ""
			for column, char in enumerate(line):
				if char.isdigit():
					value += char
					if not read_number:
						number_start = column
						read_number = True

				if not char.isdigit() and read_number:
					numbers.append(Number(int(value), row, number_start, column))
					read_number = False
					value = ""

	return (matrix, numbers)


def is_part_number(number, matrix):
	for row in matrix[max(0, number.row-1):number.row+2]:
		for char in row[max(0, number.start-1):number.end+1]:
			if not char.isdigit() and char != "." and char != "\n":
				return True
	return False

def problem3(data):
	matrix, numbers = data
	return sum(number.value if is_part_number(number, matrix) else 0 for number in numbers)

def add_gears(gears, number, matrix):
	for i, row in list(enumerate(matrix))[max(0, number.row-1):number.row+2]:
		for j, char in list(enumerate(row))[max(0, number.start-1):number.end+1]:
			if char == "*":
				gears.setdefault((i, j), []).append(number.value)

def problem3_2(data):
	matrix, numbers = data
	gears = dict()

	for number in numbers:
		add_gears(gears, number, matrix)

	return sum(gear[0] * gear[1] for gear in gears.values() if len(gear)==2)

data = parse_input("input3")

print(problem3_2(data))
