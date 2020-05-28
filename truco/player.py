from typing import List

from . import Card

class Player():
    
    def __init__(self, name: str, team: int):

        self.name = name
        self.team: int = team
        self.hand: List[Card] = []
        self.status: str = 'idle'


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

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.team == other.team