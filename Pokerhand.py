#!usr/bin/bash/python
from Card import *
suits = 'H D C S'.split(' ')
ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split(' ')

def determine_hand(hand):
	dist = get_distribution(hand)
	if repeats(hand, dist):
		return of_a_kind(hand, dist)
	else:
		if straight(dist):
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
	if(dist[9:] != [1,1,1,1]) or dist[0] != 1:
		return False
	return True

def flush(hand):
	suit = hand[0].suit
	for card in hand:
		if card.suit != suit:
			return False
	return True

def straight(dist):
	index = find_index(1, dist)
	if dist[index:index+5] == [1,1,1,1,1]:
		return True
	if dist[index-4:] == [1,1,1,1] and dist[index] == 1:
		return True
	if dist[index-3:] == [1,1,1] and dist[index:index+2] == [1,1]:
		return True
	if dist[index-2:] == [1,1] and dist[index:index+3] == [1,1,1]:
		return True
	if dist[index-1:] == [1] and dist[index:index+4] == [1,1,1,1]:
		return True
	return False

def find_index(x, iterable):#find index of element in a list
    for i, item in enumerate(iterable):
        if item == x:
            return i
    return None

def main():
	hand = [Card('H','A'),Card('C','2'),Card('H','J'),Card('H','Q'),Card('H','K')]
	print determine_hand(hand)

if __name__ == '__main__':
	main()