from flask import Flask

app = Flask(__name__)


@app.route('/')#Cuando se ralice una peticion a la pagina principal (Home)
#Se ejecuta la funcion index
def indexs():
    return 'Hola mundo desde Flask'

app.run(debug=True)