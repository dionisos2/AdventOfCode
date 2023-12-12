from collections import Counter

card_name = ["T", "J", "Q", "K", "A"]

def parse_input(file_path):
	with open(file_path, 'r') as input_file:
		hands = []
		for line in input_file.readlines():
			str_hand, bid = line.split()
			hand = []
			for card in str_hand:
				if card.isdigit():
					hand.append(int(card))
				else:
					hand.append(10+card_name.index(card))
			hands.append((hand, int(bid)))

		return hands


def compare(hand1, hand2):
	k1, k2 = kind(hand1), kind(hand2)
	if k1 > k2:
		return 1
	elif k1 < k2:
		return -1
	else:
		for card1, card2 in zip(hand1, hand2):
			if card1 > card2:
				return 1
			if card1 < card2:
				return -1
	return 0

def kind(hand):
	hand = Counter(hand)
	joker = hand[0]
	hand[0] = 0
	hand = hand.most_common()

	if hand[0][1]+joker == 1: # high card
		return 0

	if hand[0][1]+joker == 2 and hand[1][1] == 1: # one pair
		return 1

	if hand[0][1]+joker == 2 and hand[1][1] == 2: # two pair
		return 2

	if hand[0][1]+joker == 3 and hand[1][1] == 1: # three of a kind
		return 3

	if hand[0][1]+joker == 3 and hand[1][1] == 2: # full house
		return 4

	if hand[0][1]+joker == 4: # four of a kind
		return 5

	if hand[0][1]+joker == 5: # five of a kind ... lol
		return 6

def key(hand):
	return (kind(hand[0]), hand[0])

def day7(hands):
	hands = sorted(hands, key=key)
	return sum((rank+1)*hand[1] for rank, hand in enumerate(hands))

def joker(hand):
	return [value if value!=11 else 0 for value in hand]

def day7_2(hands):
	hands = [(joker(hand[0]), hand[1]) for hand in hands]
	return day7(hands)

hands = parse_input("input7")
# print(hands)
print(day7_2(hands))
