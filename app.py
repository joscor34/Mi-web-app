# Desde la libreía "flask"
# vamos a importar la clase Flask
from flask import Flask

# Desde flask_restful importamos la clase API y la clase
# Resource
from flask_restful import Api, Resource
from rutas import crear_rutas

# Vamos a crear un objeto de tipo Flask
app = Flask(__name__)

# Creamos un objeto de tipo API y como argumento
# le pasamos el objeto app

# El parametro/argumento que espera recibir es el objeto de Flask
api = Api(app)
# La API será el programa que se comunique con el dispositivo físico

crear_rutas(api)

app.run(port=8080, debug=True)
# 127.0.0.1 -> LoopBack | IP local