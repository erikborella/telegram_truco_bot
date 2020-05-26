from typing import List

from . import Card

class Player():
    
    def __init__(self, team: int):

        self.team: int = team
        self.hand: List[Card] = []
        self.status: str = ''


    def add_card_to_hand(self, card: Card) -> bool:

        if len(self.hand) >= 3:
            return False
        else:
            self.hand.append(card)
            return True


    def play(self, card_position: int) -> Card:

        try:
            return self.hand.pop(card_position)

        except:
            return None