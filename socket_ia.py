import base64
import socketio

# Crear una instancia de Socket.IO
sio = socketio.Client()

# URL del servidor Socket.IO
server_url = 'http://localhost:3000'  # Reemplaza con la URL de tu servidor Socket.IO

@sio.event
def connect():
    print('Conectado al servidor')

@sio.event
def disconnect():
    print('Desconectado del servidor')

# Ruta para enviar la imagen al servidor
@sio.event
def send_image(data):
    image_data = base64.b64decode(data)  # Decodificar los datos de imagen en base64
    # Procesar la imagen aquí según tus necesidades (guardarla en disco, realizar análisis, etc.)
    # ...

# Conexión al servidor Socket.IO
sio.connect(server_url)

# Ruta local de la imagen a enviar
image_path = 'image.jpg'  # Reemplaza con la ruta de tu imagen

# Leer la imagen y codificarla en base64
with open(image_path, 'rb') as file:
    image_data = file.read()
    base64_data = base64.b64encode(image_data).decode('utf-8')

# Enviar la imagen al servidor a través de Socket.IO
sio.emit('image', base64_data)

# Mantener el programa en ejecución hasta que se complete el envío
sio.wait()
