class Card():

    @staticmethod
    def convert_suit_to_portuguese(suit: str) -> str:
        
        return {
            'o': 'Ouro',
            'p': 'Paus',
            'e': 'Espadas',
            'c': 'Copas'
        }.get(suit, None)

    @staticmethod
    def convert_value_to_portuguese(value: int) -> str:
        
        return {
            1: 'Ás',
            10: 'Valete',
            11: 'Cavalo',
            12: 'Velha'
        }.get(value, value)

    def __init__(self, suit: str, value: int):

        self.suit = suit
        self.value = value

    def __repr__(self):
        return 'Carta: {} de {}'.format(
            self.convert_value_to_portuguese(self.value), 
            self.convert_suit_to_portuguese(self.suit)
        )