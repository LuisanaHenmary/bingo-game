from game import Game
import time
import random

if __name__=="__main__":

    game = Game()

    while True:
        game_mode = int(input("""Ingrese la modalidad de juego
1) Lograr 5 en linea.
2) Llenar todo su carton.
    """))

        for i in range(2):
            game.input_data()

        game.print_boards()
    
        for i in range(75):
            print(game.num_available_combinations())
            index = random.randint(0,game.num_available_combinations()-1)
            game.move(game_mode,index)
            time.sleep(2)
            game.print_boards()
            if game.say_bingo():
                break

        responce = int(input("""¿Quiere Parar?
1) Si.
2) No.
    """))

        game.reboot()
        if responce == 1:
            break