from flask import Flask, render_template, request
from flask_socketio import (
    SocketIO,
    send,
    emit,
    join_room,
    close_room
    )

import time
import random
from game import Game
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY']= 'secret!' #password para comunicacion segura de la aplicacion

socketio = SocketIO(app)

game = Game()

room_wait = []
disconnect_players = []


@app.route("/")
def hello():
    return render_template('index.html')

@socketio.on('disconnect') #evento cuando se desconecta alguien
def disconnect():

    """
        Si se desconecta alguien verifica si es uno o los dos jugadores que estan en juego
    """

    for  player in game.get_players_list():
        if request.sid == player["id"]:
            disconnect_players.append(player)
            send(f"Disconnect {player['PlayerName']}", to=player["room"])

@socketio.on('connect') #Cuando alguien se conecta
def connect():
    #Un anuncio para los recien conectados
    if game.get_players_list_len()==2:
        emit('anuncio',f"Juego en curso")
    else:
        emit('anuncio',f"Numero de vacante para jugar {2-game.get_players_list_len()}")


#Recibe peticiones de Jugadores a unirse el juego
@socketio.on('join')
def acceptPlayer(info):

    if game.get_players_list_len() < 2: #Si hay 0 o solo un jugador se agregara un nuevo jugador
        data= game.input_data(info["id"],info["playername"])
        room = data['room'] #Solo sala game_room recibira las combinaciones de letra y numero
        join_room(room)
        emit('accept_player', data)  
        send(info["playername"] + ' has entered the room.', to=room)
        emit('anuncio',f"Numero de vacante para jugar {2-game.get_players_list_len()}", broadcast=True)

        if game.get_players_list_len() == 2: #Si ya estando los dos emete el evento startGame al cliente
            emit('startGame')
        
    else:
        room_wait.append(info)
        send('Sala llena')

@socketio.on('game_on_going') #evento de juego en curso
def start_game(mode):

    """
        Inicia el juego que cuya modalidad se determinar por el valor de mode:
        1 -> 5 en linea
        2 -> carton lleno
    
    """

    emit('anuncio',f"Juego en curso", broadcast=True)

    for i in range(75):

        if len(disconnect_players) == 2: #Si los dos jugadores se desconectan el juego para y reinicia
            disconnect_players.clear()
            break
        
        time.sleep(3)
        index = random.randint(0,game.num_available_combinations()-1)
        letter, number = game.move(index,game_mode=int(mode))

        comb = {
            "letter":letter,
            "number":number,
            "num_com":game.num_available_combinations()
        }

        emit('send_combination',comb, to="game_room") #envia la combinacion a los integrantes de la sala y tambien la cantidad de fichas disponible
        
        winner = game.say_bingo() #Verifica si un jugaros ya tiene el bingo en True, y si es asi devuelve un diccionario con los datos del ganador
        #sino un diccionario vacio

        if len(winner) > 0:
            send(f"{winner['PlayerName']} WIN", to="game_room")
            break

    send("Fin del juego vuelva pronto", to="game_room")
    game.reboot()
    close_room('game_room')
    emit('end_game',f"Numero de vacante para jugar {2-game.get_players_list_len()}", broadcast=True)

    #Si hay jugadores en sala de espera, dos de ello se uniran al juego automaticamente 
    while True:
        if (game.get_players_list_len()==2) or (len(room_wait)==0):
            break
        player = room_wait.pop(0)
        emit('automatic_join', player,to=player["id"]) #Si tal persona se desconecto antes no habra daño
        

    
    
@socketio.on('message') # evento escuchador llamado message
def handlerMessage(playername):
    send(playername, broadcast=True) # envio de mensaje a los clientes tipo broadcast    

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000, host='localhost')