from generate_bingo import Game
import os
import time

if __name__=="__main__":

    game = Game()

    os.system("cls")
    for i in range(2):
        game.input_data()
  
    for i in range(10):
        game.print_boards()
        game.move()
        time.sleep(2)
            
    game.reset()

        