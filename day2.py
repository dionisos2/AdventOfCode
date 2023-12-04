import re
import math

colors = ["blue", "red", "green"]

def get_bag(bag):
	result = {color:0 for color in colors}
	for color in colors:
		found = re.search(rf"(\d+) {color}", bag)
		if found:
			result[color] = int(found[1])
	return result

def parse_input(file_path):
	result = []
	with open(file_path, 'r') as input_file:
		for line in input_file.readlines():
			bags = line.split(";")
			result.append([get_bag(bag) for bag in bags])

	return result


def bag_ok(bag):
	return bag["red"]<=12 and bag["green"]<=13 and bag["blue"] <= 14

def day2p1(data):
	result = 0

	for index, game in enumerate(data):
		if all(bag_ok(bag) for bag in game):
			result += index+1

	return result

def get_colors_max(game):
	result = []
	for color in colors:
		result.append(max(bag[color] for bag in game))

	return result

def day2p2(data):
	result = 0
	for game in data:
		result += math.prod(color for color in get_colors_max(game))

	return result

data = parse_input("input2")
print(day2p2(data))

