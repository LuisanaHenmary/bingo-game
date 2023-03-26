from flask import Flask, render_template
from flask_socketio import (
    SocketIO,
    send,
    emit,
    join_room,
    leave_room,
    close_room
    )

import time
import random
from Class.combinations import Combinations
from Class.players import Players

app = Flask(__name__)

app.config['SECRET_KEY']= 'secret!' #password para comunicacion segura de la aplicacion

socketio = SocketIO(app)

players = Players()
combinations = Combinations()
room_wait = []
game_start = 0

@app.route("/")
def hello():
    return render_template('index.html')

@socketio.on('disconnect') #evento escuchador
def disconnect():
    print("Desconectado")

@socketio.on('connect') #evento escuchador
def connect():
    emit('anuncio',f"Numero de vacante para jugar {2-len(players.get_players())}")


@socketio.on('evento') #evento escuchador
def evento(json):
    print("Este es el objeto Json "+json)
    emit('evento', json) # evento emisor       

#Recibe peticiones de Jugadores a unirse el juego
@socketio.on('join')
def acceptPlayer(playername):
    if len(players.get_players()) < 2:
        data = players.new_player(playername)
        room = data['room']
        join_room(room)
        emit('accept_player', data)  
        emit('anuncio',f"Numero de vacante para jugar {2-len(players.get_players())}", broadcast=True)
    else:
        room_wait.append(playername)
        send('Sala llena')
        emit('anuncio',f"Juego en curso", broadcast=True)
        

    #anuncia
    send(playername + ' has entered the room.', to=room)

    #Comienza el juego si hay solo dos jugadores
    if len(players.get_players()) == 2:
            emit('anuncio',f"Juego en curso", broadcast=True)
            for i in range(8): #Deben ser 75 el ocho es para las pruenas
                index = random.randint(0,combinations.get_num_available()-1)
                letter, number = combinations.get_combination(index)
                comb = {
                    "letter":letter,
                    "number":number
                }
                emit('send_combination',comb, to="game_room") #envia la combinacion a los integrantes de la sala
                time.sleep(5)
            send("Fin del juego vuelva pronto", to="game_room")
            players.reboot()
            combinations.reboot()
            close_room('game_room')

            #proximente trabajar en sala de espera
            
            emit('anuncio',f"Numero de vacante para jugar {2-len(players.get_players())}", broadcast=True)
    
@socketio.on('message') # evento escuchador llamado message
def handlerMessage(playername):
    send(playername, broadcast=True) # envio de mensaje a los clientes tipo broadcast    

if __name__ == "__main__":
    socketio.run(app)
    

#Anuncio Broadcast que esta Activo




# Crear tablero con jugadores


# Emitir cartones  


# Recibir aceptacion de jugadores de los cartones  


# Emitir numeros


# Comprobar si hay ganador y cerrar juego


# Anuncio broadcast de ganador

