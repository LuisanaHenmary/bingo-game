from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from Class.players import Players

app = Flask(__name__)

app.config['SECRET_KEY']= 'secret!' #password para comunicacion segura de la aplicacion

socketio = SocketIO(app)

players = Players()
room_wait = []

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
@socketio.on('accept')
def acceptPlayer(playername):
    if len(players.get_players()) < 2:
        data = players.new_player(playername)
        emit('accept_player', data)
    else:
        send('Estamos llenos')
        room_wait.append(playername)

    #anuncia
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

