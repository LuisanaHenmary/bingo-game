import random
import pandas as pd
import os

class Game:

    __combinations = []

    def __init__(self) -> None:
        self.__data_players = []
        self.generate_combinations()

    

    def unique_number(self, x, L):

        for i in range(len(L)):
        
            if x == L[i]:
                return False
            
        return True

    def column_number(self, minor, major, l):
        j = 0

        while j < 5:
            x = random.randint(minor,major)
            if  self.unique_number(x,l):
                l.append(x)
                j+=1
    
    def generate_matrix(self):
        matriz_game = {"B":[], "I":[], "N":[], "G":[], "O":[]}

        minor = 1
        major = 15

        for letter in matriz_game:
            self.column_number(minor,major,matriz_game[letter])
            minor+=15
            major+=15

        matriz_game["N"][2] = "F"

        return matriz_game

    def print_boards(self):
        
        os.system("cls")
        for player in self.__data_players:
            print(player["PlayerName"])            
            table_game = pd.DataFrame(player["board"])
            print(table_game.to_string(index=False))
            print("\n")

        
        

    def input_data(self):
        name = input("Ingrese su nombre: ")
        board = self.generate_matrix()
        self.__data_players.append({
            "PlayerName":name,
            "board": board,
            "bingo": False
        })

    def get_players(self):
        return self.__data_players

    def generate_combinations(self):

        minor = 1
        major = 15

        for letter in ["B", "I", "N", "G", "O"]:
            for x in range(minor, major+1):
                self.__combinations.append({
                    "column": letter,
                    "number": x,
                    "view": False
                })
            minor+=15
            major+=15

    def get_combinations(self):
        return self.__combinations

    def move(self):
        

        while True:
            position = random.randint(0,len(self.__combinations)-1)

            if not self.__combinations[position]["view"]:
                letter = self.__combinations[position]["column"]
                number = self.__combinations[position]["number"]
                print(letter, number)
                for player in self.__data_players:
                    for index, value in enumerate(player["board"][letter]):
                        if type(value) is not str:
                            if value == number:
                                player["board"][letter][index]="*"

                self.__combinations[position]["view"] = True
                break

    def reset(self):
        self.__data_players.clear()
        self.__combinations.clear()
        self.generate_combinations()
