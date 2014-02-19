#!/usr/bin/bash/python
from Deck import *
from Card import *
from Pokerhand import *
from Player import *
import sys

class Game(object):

	def __init__(self):
		self.deck_index = 0
		self.game_deck = Deck()
		Deck.shuffle(self.game_deck)
		self.num_players = input("How many players will be playing?")
		self.players = []
		for player in range(self.num_players):
			name = raw_input('Hello, player '+ str(player + 1) + ' What is your name?')
			person = Player(str(name))
			self.players.append(person)

def deal_cards(players):#deal 5 cards from the top of the game deck to each player
	for i in range(5): #5 cards to each player
		for player in players:
			


def main():
	game = Game()
	deal_cards(game.players)

if __name__ == '__main__':
		main()