import random

def unique_number(x, L):

    for i in range(len(L)):
        
        if x == L[i]:
            return False
            
    return True

def column_number( minor, major, l):
    j = 0

    while j < 5:
        x = random.randint(minor,major)
        if  unique_number(x,l):
            l.append(x)
            j+=1

def generate_matrix():
        
    minor = 1
    major = 15

    matriz_game = {"B":[], "I":[], "N":[], "G":[], "O":[]}

    for letter in matriz_game:
        column_number(minor,major,matriz_game[letter])
        minor+=15
        major+=15

    return matriz_game

def marking_cell(board,letter,number):
    
    for index, value in enumerate(board[letter]):
                if type(value) is not str:
                    if value == number:
                        board[letter][index]="*"

def vertical_validation(board):

    for letter in ["B", "I", "N", "G", "O"]:

        if len(set(board[letter]))==1:
            return True

    return False

def horizontal_validation(board):
    aux = []

    for position in range(5):

        aux = [board[letter][position] for letter in ["B", "I", "N", "G", "O"]]

        if len(set(aux))==1:
            return True
                
        aux.clear()
        
    return False

def diagonal_validation(board):
    diagonals = [[("B",0),("I",1),("N",2),("G",3),("O",4)],[("B",4),("I",3),("N",2),("G",1),("O",0)]]

    for diagonal in diagonals:
        aux = [board[letter][position] for letter, position in diagonal]

        if len(set(aux))==1:
            return True

        aux.clear()

    return False    
    
def full_board_validation(board):
        
    count = 0
    for letter in ["B", "I", "N", "G", "O"]:

        if len(set(board[letter])) > 1:
            break
        else:
            count+=1

    if count == 5:
        return True
        
    return False