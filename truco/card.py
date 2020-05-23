class Card():

    @staticmethod
    def convert_suit_to_portuguese(suit: str) -> str:
        
        return {
            'o': 'Ouro',
            'p': 'Paus',
            'e': 'Espadas',
            'c': 'Copas'
        }.get(suit, None)

    def __init__(self, suit, value):

        self.suit = suit
        self.value = value

    def __repr__(self):
        return 'Carta: {} de {}'.format(
            self.value, self.convert_suit_to_portuguese(self.suit)
        )