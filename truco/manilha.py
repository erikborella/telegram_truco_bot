from . import Card

class Manilha(Card):

    def __init__(self, card: Card):

        super().__init__(card.suit, card.value)

        self.real_manilha = self.get_real_manilha()


    def get_real_manilha(self) -> Card:

        real_value: int
        
        if self.value == 7:
            real_value = 10
        elif self.value == 12:
            real_value = 1
        else:
            real_value = self.value + 1

        return Card(self.suit, real_value)


    def is_manilha(self, card: Card) -> bool:

        if self.real_manilha.value == card.value and \
           self.real_manilha.suit == card.suit:
           
           self.__set_real_value(card)

           return True
        
        else:

            return False


    def __set_real_value(self, card: Card):

        real_value = {
            'o': 100,
            'e': 110,
            'c': 120,
            'p': 130
        }.get(card.suit)

        card.value = real_value


    def __repr__(self):
        
        return super().__repr__() + " => Manilha"
