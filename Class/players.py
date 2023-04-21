from .board import generate_matrix

class Players:

    """Esta clase es para registrar los jugadores que entran al juego (que maximo son 2)
    
        __data_players: Es una lista de jugadores.
    
    """

    def __init__(self) -> None:
        self.__data_players = []

    def new_player(self,id ,playername):

        """
            Agrega un diccionario que tiene los datos del jugador, y le generara un carton
            de bingo, le devolvera la info del jugador.

            Parametros de entrada:

                id (str)
                playername (str) 
            Salida:
                player (dict)

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        board = generate_matrix()
        player = {
            'id':id,
            'PlayerName':playername,
            'board': board,
            "bingo": False, #verifica si el jugador dice bingo
            'room':"game_room" #la sala donde se hara el juego
        }
        self.__data_players.append(player)
    
        return player

    def get_players(self):

        """
            Retorna la lista de jugadores.

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """
        return self.__data_players

    def reboot(self):

        """
            Vacia la lista de jugadores.

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """
        self.__data_players.clear()