from generate_bingo import Game
import os
import time
import pandas

if __name__=="__main__":

    game = Game()

    os.system("cls")
    for i in range(2):
        game.input_data()
    
    game.print_boards()

    for i in range(75):
        game.move()
        time.sleep(2)
        game.print_boards()
        if game.say_bingo():
            break
        
    

    game.diagonal_validation()
        