import os
from Class.players import Players
from Class.combinations import Combinations
from Class.board import (
    marking_cell,
    vertical_validation,
    horizontal_validation,
    diagonal_validation,
    full_board_validation,
    print_board
)


class Game:
    
    def __init__(self) -> None:
        self.__players = Players()
        self.__combinations = Combinations()

    def print_boards(self):
        
        os.system("cls")
        for player in self.__players.get_players():
            print_board(player)

    def input_data(self):
        name = input("Ingrese su nombre: ")
        self.__players.new_player(name)

    def move(self, game_mode,index):
        
        letter, number = self.__combinations.get_combination(index)
        print(f"{letter} {number}")
        
        for player in self.__players.get_players():

            marking_cell(player["board"],letter,number)

            if game_mode==1:
                if vertical_validation(player["board"]):
                    player['bingo']=True
                    return 1
                if horizontal_validation(player["board"]):
                    player['bingo']=True
                    return 1
                if diagonal_validation(player['board']):
                    player['bingo']=True
                    return 1

            if game_mode==2:
                if full_board_validation(player['board']):
                    player['bingo']=True
                    return 1
        

    def num_available_combinations(self):
        return self.__combinations.get_num_available()

    def say_bingo(self):
        for player in self.__players.get_players():
            if player["bingo"]:
                win_name = player["PlayerName"]
                print(f"{ win_name } dice BINGO")
                return True

        return False

    def reboot(self):
        self.__combinations.reboot()
        self.__players.reboot()