def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		return [line.strip() for line in input_file.readlines()]


def find_start(diagram):
	for x, line in enumerate(diagram):
		for y, char in enumerate(line):
			if char == "S":
				return  (y, x)
	raise ValueError("pas de départ")

symbols = {
	"|": [(0, 1), (0, -1)],
	"-": [(1, 0), (-1, 0)],
	"J": [(0, -1), (-1, 0)],
	"F": [(0, 1), (1, 0)],
	"L": [(0, -1), (1, 0)],
	"7": [(0, 1), (-1, 0)],
	".": [],
	"S": [(0,1),(0,-1),(1,0),(-1,0)]
	}

def get_next(previous, current, diagram):
	x, y = current
	(dx1, dy1), (dx2, dy2) = symbols[diagram[y][x]]

	if (x+dx1, y+dy1) == previous:
		return (x+dx2, y+dy2)
	else:
		return (x+dx1, y+dy1)


def valid(start, diagram):
	x, y = start
	lx, ly = len(diagram[0]), len(diagram)

	dirs = [(0,1),(0,-1),(1,0),(-1,0)]
	result = []

	for tx, ty in dirs:
		if 0 <= x+tx < lx and 0 <= y+ty < ly:
			(dx1, dy1), (dx2, dy2) = symbols[diagram[y+ty][x+tx]]

			if (x+tx+dx1, y+ty+dy1) == start or (x+tx+dx2, y+ty+dy2) == start:
				result.append((x+tx, y+ty))

	return result

def day10(diagram):
	previous = find_first(diagram)
	currents = valid(previous, diagram)
	previous = [previous for _ in currents]
	step = 1

	while True:
		for index, prev, current in enumerate(zip(previous, current))
			previous[index], currents[index] = current, get_next(previous, current, diagram)
			if valid()
			step += 1
			x, y = current
			print(current, diagram[y][x])
			input()
			if diagram[y][x] == "S":
				break

	return step/2


diagram = parse_input("input10")

print(day10(diagram))
