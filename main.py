from wsgiref.simple_server import make_server

from jinja2 import FileSystemLoader
from jinja2 import Environment

#Le decimos que nuestros archivos van a estar 
env = Environment(loader=FileSystemLoader('templates'))

def aplication(environ, start_response): #interfaz WSGI
    #environ has to many information
     #we shall write OK after the status
    status = '200 OK'

    context = {
        'username': 'Reno',
        'courses' : ['Python', 'Java', 'Django', 'Flask', 'SQL']
    }

    path = environ.get('PATH_INFO')

    if path == '/':
        #de la carpeta template trtaemos index.html
        template = env.get_template('index.html')
    elif path == '/users':
        template = env.get_template('users.html')

    #con doble asterisco python
    #descompone el diccionario en donde las keys son parametros
    response = template.render(**context) 

    start_response(status, []) #MetaData
    
    #Respuesta al cliente
    return [bytes(response, 'UTF=8')] #server returns an array of bytes

PORT = 8000

#Para utilizar la variable server con with
# it is the same as server = make_server('localhost', PORT, aplication)
with make_server('localhost', PORT, aplication) as server:
    print(f"El servidor se encuentra a la escucha en el puerto {PORT}")
    server.serve_forever()