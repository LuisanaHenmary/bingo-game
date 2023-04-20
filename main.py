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

@socketio.on('disconnect') #evento escuchador
def disconnect():
    for  player in game.get_players_list():
        if request.sid == player["id"]:
            disconnect_players.append(player)
            send(f"Disconnect {player['PlayerName']}", to=player["room"])

@socketio.on('connect') #evento escuchador
def connect():

    if game.get_players_list_len()==2:
        emit('anuncio',f"Juego en curso")
    else:
        emit('anuncio',f"Numero de vacante para jugar {2-game.get_players_list_len()}")


#Recibe peticiones de Jugadores a unirse el juego
@socketio.on('join')
def acceptPlayer(info):

    if game.get_players_list_len() < 2:
        data= game.input_data(info["id"],info["playername"])
        #data = players.new_player(info["id"],info["playername"])
        room = data['room']
        join_room(room)
        emit('accept_player', data)  
        send(info["playername"] + ' has entered the room.', to=room)
        emit('anuncio',f"Numero de vacante para jugar {2-game.get_players_list_len()}", broadcast=True)

        if game.get_players_list_len() == 2:
            emit('startGame')
        
    else:
        room_wait.append(info)
        send('Sala llena')

@socketio.on('game_on_going')
def start_game(mode):
    emit('anuncio',f"Juego en curso", broadcast=True)
    for i in range(75): #Deben ser 75 el ocho es para las pruenas

        if len(disconnect_players) == 2:
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

        emit('send_combination',comb, to="game_room") #envia la combinacion a los integrantes de la sala
        
        winner = game.say_bingo()

        if len(winner) > 0:
            send(f"{winner['PlayerName']} WIN", to="game_room")
            break

    send("Fin del juego vuelva pronto", to="game_room")
    game.reboot()
    close_room('game_room')
    emit('end_game',f"Numero de vacante para jugar {2-game.get_players_list_len()}", broadcast=True)


    while True:
        if (game.get_players_list_len()==2) or (len(room_wait)==0):
            break
        player = room_wait.pop(0)
        emit('automatic_join', player,to=player["id"])
        

    
    
@socketio.on('message') # evento escuchador llamado message
def handlerMessage(playername):
    send(playername, broadcast=True) # envio de mensaje a los clientes tipo broadcast    

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000, host='localhost')