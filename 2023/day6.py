from math import ceil

import math

def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		lines = input_file.readlines()
		times = lines[0].split(":")[1].split()
		times = [int(time) for time in times]
		distances = lines[1].split(":")[1].split()
		distances = [int(distance) for distance in distances]
		return zip(times, distances)


def day6(data):
	wins = []
	for time, distance in data:
		win = 0
		for button in range(1, time+1):
			if button * (time-button) > distance:
				win += 1
		wins.append(win)

	return math.prod(wins)

def parse_input2(file_path):
	with open(file_path, 'r') as input_file:
		lines = input_file.readlines()
		time = int(lines[0].split(":")[1].replace(" ", ""))
		distance = int(lines[1].split(":")[1].replace(" ", ""))

		return (time, distance)

def day6_2(time, distance):
	start = 1
	end = ceil(time/2)
	while end-start > 1:
		middle = start + ceil((end-start)/2)

		if middle * (time-middle) >= distance:
			end = middle
		else:
			start = middle

	return time-(end)*2+1

time, distance = parse_input2("input6")
print(day6_2(time, distance))

