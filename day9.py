def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		histories = []
		for line in input_file.readlines():
			histories.append([int(value) for value in line.split()])
	return histories


def day9(histories):
	result = 0

	for history in histories:
		next_value = history[-1]
		while any(value != 0 for value in history):
			history = [value2-value1 for value1, value2 in zip(history[:-1], history[1:])]
			next_value += history[-1]
		result += next_value

	return result

def day9_2(histories):
	result = 0

	for history in histories:
		neg = True
		next_value = history[0]
		while any(value != 0 for value in history):
			history = [value2-value1 for value1, value2 in zip(history[:-1], history[1:])]
			next_value = next_value - history[0] if neg else next_value + history[0]
			neg = not(neg)
		result += next_value

	return result

histories = parse_input("input9")

print(day9_2(histories))
