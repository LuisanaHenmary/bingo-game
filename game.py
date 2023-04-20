from Class.players import Players
from Class.combinations import Combinations
from Class.board import (
    marking_cell,
    vertical_validation,
    horizontal_validation,
    diagonal_validation,
    full_board_validation,
)

class Game:
    
    def __init__(self) -> None:
        self.__players = Players()
        self.__combinations = Combinations()

    def input_data(self,id,name):
        player = self.__players.new_player(id,name)
        return player

    def get_comb(self,index):
        letter, number = self.__combinations.get_combination(index)
        return (letter, number)

    def move(self,index, game_mode=1):
        
        letter, number = self.__combinations.get_combination(index)
        
        for player in self.__players.get_players():

            marking_cell(player["board"],letter,number)

            if game_mode==1:
                if vertical_validation(player["board"]):
                    player['bingo']=True
                    return (letter, number)
                if horizontal_validation(player["board"]):
                    player['bingo']=True
                    return (letter, number)
                if diagonal_validation(player['board']):
                    player['bingo']=True
                    return (letter, number)

            if game_mode==2:
                if full_board_validation(player['board']):
                    player['bingo']=True
                    return (letter, number)
        return (letter, number)
        

    def num_available_combinations(self):
        return self.__combinations.get_num_available()

    def get_players_list(self):
        return self.__players.get_players()

    def get_players_list_len(self):
        return len(self.__players.get_players())

    def say_bingo(self):
        for player in self.__players.get_players():
            if player["bingo"]:
                
                return player

        return {}

    def reboot(self):
        self.__combinations.reboot()
        self.__players.reboot()