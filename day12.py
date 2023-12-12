from collections import Counter
from functools import cache

def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		result = []
		for line in input_file.readlines():
			springs, groups = line.split(" ")
			groups = tuple([int(value) for value in groups.split(",")])
			result.append((springs, groups))
		return result

def valid(springs, groups):
	broken, unknown = springs.count("#"), springs.count("?")

	return broken <= sum(groups) <=  broken + unknown

def next_possibilities(springs, groups):
	group = groups[0]
	new_groups = groups[1:]
	result = []

	for index, spring in enumerate(springs):

		part = springs[index:index+group]
		if index + group > len(springs) or any(v=="." for v in part): #unsure
			if spring=="#":
				break
			continue

		new_springs = springs[index+group+1:]
		if (index + group == len(springs) or springs[index+group] != "#") and valid(new_springs, new_groups):
			result.append((new_springs, new_groups))

		if spring == "#":
			break

	return result

# def get_arrangement_stack(springs, groups):
# 	stack = Counter([(springs, groups)])
# 	cache = Counter()
# 	result = 0

# 	while stack.total() > 0:
# 		(springs, groups), count = stack.popitem()

# 		if len(groups) == 0:
# 			result += count
# 		else:
# 			possibilities = next_possibilities(springs, groups)
# 			for possibility in possibilities:
# 				stack[possibility] += count

# 	return result

@cache
def get_arrangement(springs, groups):
	result = 0

	for next_springs, next_groups  in next_possibilities(springs, groups):
		if len(next_groups) == 0:
			result += 1
		else:
			result += get_arrangement(next_springs, next_groups)

	return result

def day12(data):
	return sum(get_arrangement(springs, groups) for springs, groups in data)

def day12_2(data):
	unfolded=[]
	for springs, groups in data:
		springs = "?".join([springs for _ in range(5)])
		unfolded.append((springs, groups*5))

	return day12(unfolded)

data = parse_input("input12")

print(day12_2(data))

