from math import inf

class Map:
	def __init__(self, source, destination, map_ranges):
		self.source = source
		self.destination = destination
		self.map_ranges = map_ranges

	def convert(self, source):
		for destination_start, source_start, range_length in self.map_ranges:
			if source_start <= source <= source_start + range_length:
				return source + destination_start - source_start
		return source

	@classmethod
	def read_map(cls, lines, index):
		name = lines[index].split()[0]
		index += 1
		source, destination = name.split("-to-")
		map_ranges = []
		while True:
			if index>=len(lines) or lines[index] == "\n":
				break

			dest, src, rang = [int(value) for value in lines[index].split()]
			map_ranges.append((dest, src, rang))
			index += 1

		return (index, cls(source, destination, map_ranges))

def parse_input(file_path, Cls=Map):
	maps = dict()
	with open(file_path, 'r') as input_file:
		index = 0
		lines = input_file.readlines()

		seeds = [int(seed) for seed in lines[0].split(":")[1].split()]
		index += 2

		while index < len(lines):
			index, new_map = Cls.read_map(lines, index)
			maps[new_map.source] = new_map
			index += 1

	return (seeds, maps)

def get_chain(maps):
	source = "seed"
	result = []

	while True:
		current_map = maps[source]
		result.append(current_map)
		source = current_map.destination
		if current_map.destination == "location":
			break

	return result

def day5(seeds, maps):
	maps = get_chain(maps)
	locations = []

	for seed in seeds:
		for current_map in maps:
			seed = current_map.convert(seed)
		locations.append(seed)

	return min(locations)

# -------------------------------------------------- PROBLEM 2 --------------------------------------------------
def intersect(current_range, range_map):
	rc = (current_range[0], current_range[0] + current_range[1] - 1)
	rmap = (range_map[0], range_map[0] + range_map[1] - 1)

	if rc[0] >= rmap[0] and rc[1] <= rmap[1]: # inside → keep nothing
		return ([], current_range)

	if rc[1] < rmap[0] or rc[0] > rmap[1]: # no intersection → keep all
		return ([current_range], None)

	if rc[0] <= rmap[0] and rc[1] <= rmap[1]:
		to_keep = (rc[0], rmap[0]-rc[0])
		to_transform = (rmap[0], rc[1]-rmap[0]+1) # rc[1]-rc[0]+1
		return ([to_keep], to_transform)

	if rc[0] >= rmap[0] and rc[1] >= rmap[1]:
		to_keep = (rmap[1]+1, rc[1]-rmap[1])
		to_transform = (rc[0], rmap[1]-rc[0]+1)
		return ([to_keep], to_transform)

	if rc[0] < rmap[0] and rc[1] > rmap[1]: # in the middle
		to_keep1 = (rc[0], rmap[0]-rc[0])
		to_transform = (rmap[0], rmap[1]-rmap[0]+1)
		to_keep2 = (rmap[1]+1, rc[1]-rmap[1])
		return ([to_keep1, to_keep2], to_transform)

class MapRange(Map):
	def convert_ranges(self, ranges):
		result = set()

		for destination_start, source_start, range_length in self.map_ranges + [(0, 0, inf)]:
			to_keeps = set()
			for current_range in ranges:
				to_keep, to_transform = intersect(current_range, (source_start, range_length))

				if to_transform != None:
					shift = destination_start - source_start
					result.add((to_transform[0]+shift, to_transform[1]))

				to_keeps |= set(to_keep)
			ranges = to_keeps

		return result|to_keeps

def day5_2(seeds, maps):
	seed_ranges = [(seed, seed_range) for seed, seed_range in zip(seeds[::2], seeds[1::2])]
	maps = get_chain(maps)
	locations = []
	for seed_range in seed_ranges:
		current_ranges = [seed_range]

		for current_map in maps:
			current_ranges = current_map.convert_ranges(current_ranges)

		locations.append(min(ranges[0] for ranges in current_ranges))
	return min(locations)

seeds, maps = parse_input("input5", MapRange)

print(day5_2(seeds, maps))

def test():
	rmap = (4, 4)
	print(intersect((3, 3), rmap))
	print(intersect((1, 2), rmap))
	print(intersect((8, 2), rmap))
	print(intersect((5, 2), rmap))
	print(intersect((2, 8), rmap))

# test()
