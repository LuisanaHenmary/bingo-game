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


    """
        Esta clase es la mecanica del juego.

        __players es la instancia de la clase Players
        __combinations es la instancia de la clase es Combinations

    """
    
    def __init__(self) -> None:
        self.__players = Players()
        self.__combinations = Combinations()

    def input_data(self,id,name):

        """
            Registra un nuevo jugador.

            Parametros de entrada:

                id (str)
                name (str) 
            Salida:
                player (dicy)

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """
        player = self.__players.new_player(id,name)
        return player

    def move(self,index, game_mode=1):

        """
            Obtiene una combinacion de la posicion index de la lista de combinaciones y marca
            en el carton de cada jugador y verifica si uno de los juegadores logra un 5 en linea
            (vertical, horizontal o diagonal) si game_mode vale 1, o un carton lleno si game_mode 
            vale 2, para cambiar el bingo de tal jugador en True, y retorna la tupla para detener
            el ciclo
        
            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """
        
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

        """
            Retorna el numero de combinaciones diponibles.
            
            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        return self.__combinations.get_num_available()

    def get_players_list(self):

        """
            Retorna la lista de jugadores.

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        return self.__players.get_players()

    def get_players_list_len(self):

        """
            Retorna la longitud de la lista de jugadores.

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        return len(self.__players.get_players())

    def say_bingo(self):
        """
            Verifica si uno de los jugadores tienen el valor de bingo en True.

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        for player in self.__players.get_players():
            if player["bingo"]:
                
                return player

        return {}

    def reboot(self):

        """
            Reinicia la lista de jugadores y combinaciones.

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        self.__combinations.reboot()
        self.__players.reboot()