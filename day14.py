def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		return [line.strip() for line in input_file.readlines()]

def pp(matrix):
	for line in matrix:
		print(line)

def day14(platform):
	blocked = [0 for _ in platform[0]]
	lrow = len(platform)

	result = 0
	for column, value in enumerate(blocked):
		for row, line in enumerate(platform):
			block = platform[row][column]
			if block == "#":
				blocked[column] = row + 1
			if block == "O":
				result += (lrow) - blocked[column]
				blocked[column] += 1

	return result

# 136
platform = parse_input("input14")
print(sum(line.count("O") for line in platform))
exit()
print(day14(platform))
