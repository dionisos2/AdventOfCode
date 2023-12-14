def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		return [line.strip() for line in input_file.readlines()]


def find_start(diagram):
	for x, line in enumerate(diagram):
		for y, char in enumerate(line):
			if char == "S":
				return  (y, x)
	raise ValueError("Start not found")

symbol_dirs = {
	"|": [(0, 1), (0, -1)],
	"-": [(1, 0), (-1, 0)],
	"J": [(0, -1), (-1, 0)],
	"F": [(0, 1), (1, 0)],
	"L": [(0, -1), (1, 0)],
	"7": [(0, 1), (-1, 0)],
	".": [],
	"S": [(0,1),(0,-1),(1,0),(-1,0)]
	}


def add(v1, v2):
	return tuple(x+y for x, y in zip(v1, v2))

def symbol(current, diagram):
	return diagram[current[1]][current[0]]

def valid(current, direction, diagram, visited):
	x, y = current
	dx, dy = direction
	nx, ny = x+dx, y+dy
	lx, ly = len(diagram[0]), len(diagram)

	if not(0 <= nx < lx and 0 <= ny < ly) or visited[ny][nx]!="0":
		return False

	if (-dx, -dy) in symbol_dirs[symbol((nx, ny), diagram)]:
		return True

	return False

def find_next(current, diagram, visited, uniq=False):
	dirs = symbol_dirs[symbol(current, diagram)]
	result = []

	for direction in dirs:
		if valid(current, direction, diagram, visited):
			new = add(current, direction)
			result.append(new)

	if uniq:
		if len(result)==1:
			return result[0]
		if len(result)==2:
			x, y = result[0]
			if diagram[y][x] == "S":
				return result[1]
			else:
				return result[0]
		raise ValueError("Should not be possible")
	else:
		return result


def pp(diagram):
	for line in diagram:
		print(line)

def day10(diagram):
	visited = clear_visited(diagram)
	start = find_start(diagram)
	currents = find_next(start, diagram, visited)

	for current in currents:
		step = 0
		while True:
			x, y = current
			visited[y][x] = symbol(current, diagram)

			current = find_next(current, diagram, visited, True)
			if current == None:
				break
			step += 1

			if symbol(current, diagram)=="S":
				pp(visited)
				return (step+1)/2

	return False

def clear_visited(diagram):
	return [["0" for _ in line] for line in diagram]

def sub(v1, v2):
	return tuple(x-y for x, y in zip(v1, v2))

def correct_symbol(first, current, last):
	dir1 = sub(first, current)
	dir2 = sub(last, current)
	correct_dirs = sorted([dir1, dir2])

	for sym, dirs in symbol_dirs.items():
		if sorted(dirs) == correct_dirs:
			return sym

def find_loop(diagram):
	start = find_start(diagram)
	visited = clear_visited(diagram)
	currents = find_next(start, diagram, visited)

	for current in currents:
		first = current
		while True:
			x, y = current
			visited[y][x] = symbol(current, diagram)

			last = current
			current = find_next(current, diagram, visited, True)
			if current == None:
				break

			if symbol(current, diagram)=="S":
				S = correct_symbol(first, current, last)
				x, y = current
				visited[y][x] = S
				return visited
		visited = clear_visited(diagram)
	raise ValueError("impossible…")

def day10_2(diagram):
	visited = find_loop(diagram)
	area = 0

	for line in visited:
		in_loop = False
		for visit in line:
			if visit=="|" or visit=="J" or visit=="L":
				in_loop = not(in_loop)
			elif visit=="0" and in_loop:
				area += 1

	return area

diagram = parse_input("input10")

print(day10_2(diagram))
