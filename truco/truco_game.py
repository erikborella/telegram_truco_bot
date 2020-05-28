from typing import List
from . import Deck, Player, Manilha

class Truco():
    
    def __init__(self, players_quantity):

        if players_quantity == 2 or \
           players_quantity == 4 or \
           players_quantity == 6:

            self.players_quantity = players_quantity
        else:
            raise Exception("Só é permitido 2, 4 ou 6 jogadores")
        
        self.deck = Deck()
        self.players: List[Player] = []
        self.dealer = players_quantity-1
        self.manilha: Manilha


    def add_player(self, player:Player) -> dict:

        if player.team != 1 and player.team != 2:
            return {
                'status': False,
                'message': 'Numero de time não permitido'
            }

        elif len(self.players) >= self.players_quantity:
            return {
                'status': False,
                'message': 'A mesa já está lotada'
            }
        
        elif self.__is_player_already_added(player):
            return {
                'status': False,
                'message': '{} já está na mesa'.format(player.name)
            }
        
        elif self.__is_team_complete(player.team):
            return {
                'status': False,
                'message': 'O time já está completo'
            }
        
        else:
            self.players.append(player)
            return {
                'status': True,
                'message': '{} entrou na mesa'.format(player.name)
            }


    def start(self) -> bool:
        
        if len(self.players) != self.players_quantity:
            return False

        else:
            self.__organize_players_order()
            self.__give_cards()
            
            self.manilha = Manilha(self.deck.get_card())

            self.__set_next_dealer()
            
            return True


    def __is_player_already_added(self, player: Player) -> bool:
        return player in self.players


    def __is_team_complete(self, team_number: int) -> bool:

        max_group_qnt = self.players_quantity / 2
        group_players_count = 0

        for player in self.players:
            if player.team == team_number:
                group_players_count += 1
        
        return group_players_count >= max_group_qnt


    def __give_cards(self):

        for _ in range(3):
            for player in self.players:
                player.add_card_to_hand(self.deck.get_card())

    
    def __set_next_dealer(self):

        self.players[self.dealer].status = 'idle'

        self.dealer += 1

        if self.dealer >= self.players_quantity:
            self.dealer = 0
        
        self.players[self.dealer].status = 'playing'

    
    def __organize_players_order(self):

        team1_players: List[Player] = []
        team2_players: List[Player] = []

        for player in self.players:

            if player.team == 1:
                team1_players.append(player)

            elif player.team == 2:
                team2_players.append(player)

        self.players: List[Player] = []

        for i in range(self.players_quantity // 2):
            self.players.append(team1_players[i])
            self.players.append(team2_players[i])
            