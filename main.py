from generate_bingo import Game
import os
import time
import json

if __name__=="__main__":

    game_mode = int(input("""Ingrese la modalidad de juego
1) Lograr 5 en linea.
2) Llenar todo su carton.
    """))

    print(game_mode)

    game = Game()

    
    os.system("cls")
    for i in range(2):
        game.input_data()
    
    game.print_boards()

    for i in range(75):
        game.move(game_mode)
        time.sleep(2)
        game.print_boards()
        if game.say_bingo():
            break


        
    

    game.diagonal_validation()
        