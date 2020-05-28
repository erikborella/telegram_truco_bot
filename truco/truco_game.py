from typing import List
from . import Deck, Player

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


    def __is_player_already_added(self, player: Player) -> bool:
        return player in self.players


    def __is_team_complete(self, team_number: int) -> bool:

        max_group_qnt = self.players_quantity / 2
        group_players_count = 0

        for player in self.players:
            if player.team == team_number:
                group_players_count += 1
        
        return group_players_count >= max_group_qnt