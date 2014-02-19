#!usr/bin/bash/python

class Card(object):
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def print_card(self):
		print self.suit + ',' + self.rank