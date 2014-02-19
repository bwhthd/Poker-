#!usr/bin/bash/python
from Card import *
from random import shuffle

class Deck(object):

	def __init__(self):
		suits = 'H D C S'.split(' ')
		ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split(' ')	
		self.cards = []
		for suit in suits:
			for rank in ranks:
				card = Card(suit,rank)
				self.cards.append(card)

	def shuffle(self):
		shuffle(self.cards)

	def print_deck(self):
		for card in self.cards:
			Card.print_card(card)
	
def main():
	new_deck = Deck()
	Deck.print_deck(new_deck)
	Deck.shuffle(new_deck)
	print '================================'
	Deck.print_deck(new_deck)


if __name__ == '__main__':
		main()