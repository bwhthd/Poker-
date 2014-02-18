#!usr/bin/bash/python
import sys
suits = 'H D C S'.split(' ')
ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split(' ')

class card(object):
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

def determine_hand(hand):
	dist = get_distribution(hand)
	if repeats(hand, dist):
		return of_a_kind(hand, dist)
	else:
		if straight(hand, dist):
			if flush(hand):
				if royal(dist):
					return "Royal Flush"
				return "Straight Flush"
			return "Straight"
		return "High Card"

def get_distribution(hand):
	num_of_rank = [0,0,0,0,0,0,0,0,0,0,0,0,0]
	for card in hand:
		i = find_index(card.rank, ranks)
		num_of_rank[i] += 1
	return num_of_rank

def repeats(hand, dist):
	for card in hand:
		if dist[find_index(card.rank, ranks)] >= 2:
			return True
	return False

def of_a_kind(hand, dist):
	for i in range(13):
		if dist[i] == 4:
			return 'Four of a Kind'
		elif dist[i] == 3:
			return 'Three of a Kind'
		elif dist[i] == 2:
			return 'Two Pair'

def royal(dist):
	return False

def flush(hand):
	suit = hand[0].suit
	for card in hand:
		if card.suit != suit:
			return False
	return True

def straight(hand, dist):
	index = find_index(1, dist)
	for i in dist[index:index+5]:
		if dist[i] == 0:
			return False
	return True

def find_index(x, iterable):#find index of element in a list
    for i, item in enumerate(iterable):
        if item == x:
            return i
    return None

def main():
	hand = [card('H','A'),card('H','8'),card('H','3'),card('H','4'),card('H','5')]
	print determine_hand(hand)

if __name__ == '__main__':
	main()