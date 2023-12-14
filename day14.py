def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		return [list(line.strip()) for line in input_file.readlines()]

def pp(matrix):
	print()
	for line in matrix:
		print(line)
	print()

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

def get_block(platform, coord):
	row, column = coord
	return platform[row][column]

def swap_blocks(platform, coord1, coord2):
	row1, column1 = coord1
	row2, column2 = coord2
	platform[row1][column1], platform[row2][column2] = platform[row2][column2], platform[row1][column1]

def slide(platform, coords):
	for row, line in enumerate(coords):
		last_free = 0
		for column, coord in enumerate(line):
			block = get_block(platform, coord)
			if block == "#":
				last_free = column + 1
			if block == "O" and last_free < len(line):
				last_coord = line[last_free]
				swap_blocks(platform, last_coord, coord)
				last_free += 1

def create_coords(platform):
	rows = list(range(len(platform)))
	columns = list(range(len(platform)))

	west_coords = [[(row, column) for column in columns] for row in rows]
	east_coords = [[(row, column) for column in reversed(columns)] for row in rows]
	north_coords = [[(row, column) for row in rows] for column in columns]
	south_coords = [[(row, column) for row in reversed(rows)] for column in columns]

	return (north_coords, west_coords, south_coords, east_coords)

def cycle(platform, coords):
	for coord in coords:
		slide(platform, coord)

def hash_platform(platform):
	result = ""
	for line in platform:
		result += "".join(line) + "\n"

	return hash(result)

def get_weight(platform):
	result = 0
	lrow = len(platform)
	for row, line in enumerate(platform):
		for char in line:
			if char == "O":
				result += lrow - row
	return result

def day14_2(platform):
	num_cycle = 1000000000
	coords = create_coords(platform)

	cycle_hashs = {hash_platform(platform):0}
	weights = [get_weight(platform)]

	for index in range(1,1000):
		cycle(platform, coords)
		cycle_hash = hash_platform(platform)

		if cycle_hash in cycle_hashs:
			last_index = cycle_hashs[cycle_hash]
			shift = index - last_index
			# s+S*X+R = 100
			# R = 100-s-S*X % S
			# R = (100-s) % S
			correct_index = last_index + (num_cycle-last_index)%shift
			return weights[correct_index]
		else:
			cycle_hashs[cycle_hash] = index
			weights.append(get_weight(platform))
	return 0

platform = parse_input("input14")

print(day14_2(platform))
