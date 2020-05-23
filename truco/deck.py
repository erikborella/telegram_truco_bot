import random
from typing import List
from .card import Card

class Deck:

    def __init__(self):
        self.deck: List[Card] = []
        self.taken: List[Card] = []

        self.__initDeck()
        self.shuffle_deck()

    def __initDeck(self):

        suits = ('o', 'p', 'e', 'c')
        values = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)

        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.deck.append(card)

    def shuffle_deck(self):

        random.shuffle(self.deck)


    def get_card(self) -> Card:

        taken_card = self.deck.pop()
        self.taken.append(taken_card)
        return taken_card


    def reset_deck(self):

        for taken_card in self.taken:
            self.deck.append(taken_card)
            
        self.taken = []

        self.shuffle_deck()
