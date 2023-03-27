# bingo-game
Es un prototipo para un juego de bingo que solo se ejecutara en consola

# Se requiere un entorno virtual para ejecutarlo por las dependencias pandas, Flask y Flask-SocketIO

# Creacion del entorno virtual
py -m venv myvenv

# Activacion del entorno virtual
al menos ingrese la ruta del archivo activate.bat, que esta dentro de la carpeta Scripts.
myvenv\Scripts\activate.bat (con Windows)

# Para obterner la dependencias usadas en esto, se debe tener el entorno activado
pip install -r dependencies.txt

# Para la lista de dependencias
pip list

# Para ejecutar

# La version sin sockets
python main.py 

# La version con sockets
python main2.py 
