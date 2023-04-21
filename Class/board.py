import random

def unique_number(x, L):

    """
        Verifica si en la lista L existe un numero igual a x.

        Parametros de entrada:

            x (int)
            L (list) 
        Salida:
            Retorna False si el valor de x existe en L, sino es asi por defecto retornara True.
    
    """

    for i in range(len(L)): 
        
        if x == L[i]:
            return False
            
    return True

def column_number( minor, major, l):


    """
        Construira una de las columnas del carton de bingo que sera el lista l, la columna estara
        compuesta por 5 numeros, sin repetir, que estaran entre minor (incluido) y major (incluido).
        Por ejemplo en la columna B tendra 5 numeros sin repetir que estaran entre 1 (incluido) y
        15 (incluido).  

        Parametros de entrada:

            minor (int)
            major (int)
            l (list)
    """


    j = 0

    while j < 5:
        x = random.randint(minor,major)
        if  unique_number(x,l):
            l.append(x)
            j+=1

def generate_matrix():
    
    """
        El carton de bingo sera un diccionario donde las llaves seran las letras B, I, N, G, O
        y su valor una lista la cual tendra los 5 numeros no repetidos. Importante saber que:

        Los 5 valores de B estaran entre 1 (incluido) y 15 (incluido)
        Los 5 valores de I estaran entre 16 (incluido) y 30 (incluido)
        Los 5 valores de N estaran entre 31 (incluido) y 45 (incluido)
        Los 5 valores de G estaran entre 46 (incluido) y 60 (incluido)
        Los 5 valores de O estaran entre 61 (incluido) y 75 (incluido)

        Salida:
            matriz_game (dict)

    """

    minor = 1
    major = 15

    matriz_game = {"B":[], "I":[], "N":[], "G":[], "O":[]}

    for letter in matriz_game:
        column_number(minor,major,matriz_game[letter])
        minor+=15
        major+=15

    return matriz_game

def marking_cell(board,letter,number):

    """
        Verifica si en diccionario board existe un numero igual a number en la lista
        cuya llave en el diccionario es letter, si es asi el numero se reemplaza por
        un asterico (*).

        Parametros:
            board (dict)
            letter (str)
            number (int)
    """
    
    for index, value in enumerate(board[letter]):
                if type(value) is not str:
                    if value == number:
                        board[letter][index]="*"

def vertical_validation(board):

    """
        Verifica si se logra un 5 en fila de manera vertical en board.
        
        Nota: recordar que los cojuntos nunca tienen valores repetidos, si una lista, que tiene valores repetido,
        se convierte en conjunto con set() solo saldra ese valor una vez, por ejemplo set([1,*,*,*,*]), el conjunto
        quedaria {1,*} con logitud 2 y si set([*,*,*,*,*]) el conjunto queda {*} de longitud 1

        Parametros:
            board (dict)
    """

    for letter in ["B", "I", "N", "G", "O"]:

        #Convierte la lista de letter en un conjunto y verifica si solo tiene un valor el conjunto
        if len(set(board[letter]))==1: 
            
            return True

    return False

def horizontal_validation(board):

    """
        Verifica si se logra un 5 en fila de manera horizontal en board. 
        
        Nota: recordar que los cojuntos nunca tienen valores repetidos, si una lista, que tiene valores repetido,
        se convierte en conjunto con set() solo saldra ese valor una vez, por ejemplo set([1,*,*,*,*]), el conjunto
        quedaria {1,*} con logitud 2 y si set([*,*,*,*,*]) el conjunto queda {*} de longitud 1

        Parametros:
            board (dict)
    """

    aux = []

    for position in range(5):

        #se requiere una lista auxiliar para obtener los valores de tal posicion de cada columna
        aux = [board[letter][position] for letter in ["B", "I", "N", "G", "O"]]

        if len(set(aux))==1:
            return True
                
        aux.clear() 
        
    return False

def diagonal_validation(board):

    """
        Verifica si se logra un 5 en fila de manera diagonal en board. 
        
        Nota: recordar que los cojuntos nunca tienen valores repetidos, si una lista, que tiene valores repetido,
        se convierte en conjunto con set() solo saldra ese valor una vez, por ejemplo set([1,*,*,*,*]), el conjunto
        quedaria {1,*} con logitud 2 y si set([*,*,*,*,*]) el conjunto queda {*} de longitud 1

        Parametros:
            board (dict)
    """

    #contiene la posiciones que conforma la dos diagonales
    diagonals = [[("B",0),("I",1),("N",2),("G",3),("O",4)],[("B",4),("I",3),("N",2),("G",1),("O",0)]]

    for diagonal in diagonals:
        aux = [board[letter][position] for letter, position in diagonal] #de nuevo asar un auxiliar

        if len(set(aux))==1:
            return True

        aux.clear()

    return False    
    
def full_board_validation(board):


    """
        Verifica si se logra que todas las columna esten marcadas en board. 
        
        Nota: recordar que los cojuntos nunca tienen valores repetidos, si una lista, que tiene valores repetido,
        se convierte en conjunto con set() solo saldra ese valor una vez, por ejemplo set([1,*,*,*,*]), el conjunto
        quedaria {1,*} con logitud 2 y si set([*,*,*,*,*]) el conjunto queda {*} de longitud 1

        Parametros:
            board (dict)
    """
    
        
    count = 0 #Para medir cuantas columnas estan completamente marcadas (que tenga puros *)
    for letter in ["B", "I", "N", "G", "O"]:
        if len(set(board[letter])) > 1:
            break
        else:
            count+=1

    if count == 5:
        return True
        
    return False