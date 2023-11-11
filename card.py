import pandas as pd
import numpy as np

## SUITS
# Spades --> 3
# Hearts --> 2
# Diamonds --> 1
# Clubs --> 0

## RANKS
# Jack --> 11
# Queen --> 12
# King --> 13

class Card:
    suits = ['Clubs', "Diamonds", 'Hearts', 'Spades']
    ranks = ['narf', 'Ace', '2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + ' of ' + self.suits[self.suit])