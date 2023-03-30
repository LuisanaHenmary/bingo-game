from .board import generate_matrix

class Players:

    def __init__(self) -> None:
        self.__data_players = []

    def new_player(self,id ,playername):

        board = generate_matrix()
        player = {
            'id':id,
            'PlayerName':playername,
            'board': board,
            "bingo": False,
            'room':"game_room"
        }
        self.__data_players.append(player)
    
        return player

    def get_players(self):
        return self.__data_players

    def reboot(self):
        self.__data_players.clear()