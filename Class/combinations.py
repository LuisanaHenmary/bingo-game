class Combinations:

    """Esta clase es para las 75 combinaciones letra-numero
    
        __combinations: Es una lista que contendra las 75 combinaciones letra-numero
    
    """

    __combinations = []

    def __init__(self) -> None:

        """
            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        self.generate_combinations()

    def generate_combinations(self):

        """
            Agrega un diccionario donde column tendra el valor de la letra y number el
            numero, respetando este criterio:

            Los numeros de B estaran entre 1 (incluido) y 15 (incluido)
            Los numeros de I estaran entre 16 (incluido) y 30 (incluido)
            Los numeros de N estaran entre 31 (incluido) y 45 (incluido)
            Los numeros de G estaran entre 46 (incluido) y 60 (incluido)
            Los numeros de O estaran entre 61 (incluido) y 75 (incluido)

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos

        """

        minor = 1
        major = 15

        for letter in ["B", "I", "N", "G", "O"]:
            for x in range(minor, major+1):
                self.__combinations.append({
                    "column": letter,
                    "number": x
                })
            minor+=15
            major+=15

    def get_combination(self,index):

        """
            Obtiene la combinacion de  __combinations[index].

            Parametros:
                index (int)

            Salida:
                Una tupla

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        mov = self.__combinations.pop(index)

        letter = mov["column"]
        number = mov["number"]

        return (letter, number)

    def reboot(self):
        """
            Primero limpia __combinations volviendolo un array vacio y vuelve ha generar las 75 combinaciones.

            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """

        self.__combinations.clear()
        self.generate_combinations()

    def get_num_available(self):

        """
            Retorna la longitud de __combinations
            
            self es solo para acceder a una de las propiedades de las clase, ya sea atributos
            o metodos
        """
        return len(self.__combinations)
