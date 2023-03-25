from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)

app.config['SECRET_KEY']= 'secret!' #password para comunicacion segura de la aplicacion

socketio = SocketIO(app)

@app.route("/")
def hello():
    return render_template('index.html')


@socketio.on('evento') #evento escuchador
def evento(json):
    print("Este es el objeto Json "+json)
    emit('evento', json) # evento emisor       

@socketio.on('message') # evento escuchador llamado message
def handlerMessage(msg):
    print("Mensaje :" + msg)
    send(msg, broadcast =True) # envio de mensaje a los clientes tipo broadcast

    

if __name__ == "__main__":
    socketio.run(app)

#Anuncio Broadcast que esta Activo


#Recibe peticiones de Jugadores a unirse el juego


# Crear tablero con jugadores


# Emitir cartones  


# Recibir aceptacion de jugadores de los cartones  


# Emitir numeros


# Comprobar si hay ganador y cerrar juego


# Anuncio broadcast de ganador

