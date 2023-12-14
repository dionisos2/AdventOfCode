def parse_input(file_path):
	scratchcards = []

	with open(file_path, 'r') as input_file:
		for line in input_file.readlines():
			winnings_numbers, numbers = [line.strip().split() for line in line.split(":")[1].split("|")]
			winnings_numbers = set([int(num) for num in winnings_numbers])
			numbers = set([int(num) for num in numbers])
			scratchcards.append((winnings_numbers, numbers))
	return scratchcards

def problem4(data):
	return sum(int(2**(len(numbers&winnings)-1)) for numbers, winnings in data)


def problem4_2(data):
	cards = [[len(numbers&winnings), 1] for numbers, winnings in data]

	result = 0
	for index, card in enumerate(cards):
		result += card[1]
		for winned_cards in cards[index+1:index+card[0]+1]:
			winned_cards[1] += card[1]

	return result

data = parse_input("input4")
print(problem4_2(data))
