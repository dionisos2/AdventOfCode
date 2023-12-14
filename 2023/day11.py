from math import inf

def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		return [line.strip() for line in input_file.readlines()]

def pp(matrix):
	for line in matrix:
		print(line)

def get_galaxies(univers):
	result = []
	for i, line in enumerate(univers):
		for j, location in enumerate(line):
			if location == "#":
				result.append([i, j])
	return result

def expand(galaxies, univers, by_line, speed = 2):
	gals = dict([])

	if by_line:
		dim = 0
	else:
		dim = 1
		univers = zip(*univers)

	for galaxy in galaxies:
		i, j = galaxy
		gals.setdefault(galaxy[dim], []).append([i, j])

	expansion = 0
	for index, line in enumerate(univers):
		if all(location == "." for location in line):
			expansion += speed-1
		else:
			for galaxy in gals[index]:
				galaxy[dim] += expansion

	return [galaxy for galaxies in gals.values() for galaxy in galaxies]

def distance(g1, g2):
	i1, j1 = g1
	i2, j2 = g2
	return abs(i2-i1) + abs(j2-j1)

def day11(univers):
	galaxies = get_galaxies(univers)
	galaxies = expand(galaxies, univers, True, 1000000)
	galaxies = expand(galaxies, univers, False, 1000000)

	distances = []
	for index, galaxy1 in enumerate(galaxies):
		for galaxy2 in galaxies[index+1:]:
			distances.append(distance(galaxy1, galaxy2))

	return sum(distances)

univers = parse_input("input11")

print(day11(univers))
