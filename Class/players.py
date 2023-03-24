from .board import generate_matrix

class Players:

    def __init__(self) -> None:
        self.__data_players = []

    def new_player(self, playername):

        board = generate_matrix()
        player = {
            'PlayerName':playername,
            'board': board,
            "bingo": False
        }
        self.__data_players.append(player)

    def get_players(self):
        return self.__data_players

    def reboot(self):
        self.__data_players.clear()