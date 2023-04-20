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

# Para actulizar dependencies.txt conforme agregue nuevas librerias al entorno virtual
pip freeze > dependencies.txt


# Para la lista de dependencias
pip list

# Para ejecutar

# Modulo principal
python main.py