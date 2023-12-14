import re
import math

def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		lines = input_file.readlines()
		instructions = lines[0].strip()
		nodes = dict()
		for line in lines[2:]:
			values = re.search(r"(\w+)\W*(\w+)\W*(\w+)", line)
			nodes[values[1]] = (values[2], values[3])

		return (instructions, nodes)


def day8(instructions, nodes, current="AAA"):
	step = 0
	index = 0

	while current[-1] != "Z":
		if instructions[index] == "L":
			current = nodes[current][0]
		else:
			current = nodes[current][1]

		index = (index+1)%len(instructions)
		step += 1

	return step

def day8_2(instructions, nodes):
	currents = [name for name in nodes.keys() if name[-1]=="A"]

	steps = [day8(instructions, nodes, current) for current in currents]

	return math.lcm(*steps)

instructions, nodes = parse_input("input8")

print(day8_2(instructions, nodes))
