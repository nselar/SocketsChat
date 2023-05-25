import socket
import threading
import sys

def handle_client(client_socket, client_address):
    while True:
        # Esperar a recibir datos del cliente
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Enviar los datos recibidos a todos los clientes conectados
        message = f'{client_address[1]} ({clients[client_socket]}): {data}'
        print(message)
        broadcast(message)

    # Cerrar la conexión con el cliente
    client_socket.close()
    del clients[client_socket]
    print(f'Cliente {client_address[1]} desconectado.')

def broadcast(message):
    # Enviar el mensaje a todos los clientes conectados
    for client_socket in clients:
        client_socket.send(message.encode('utf-8'))

def start_server():
    global clients
    clients = {}

    # Configurar el socket del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.40', 12345))
    server_socket.listen(5)
    print('Servidor iniciado. Esperando conexiones...')

    while True:
        # Aceptar conexiones de clientes
        client_socket, client_address = server_socket.accept()

        # Leer el nombre del cliente de los argumentos en la línea de comandos
        name = client_socket.recv(1024).decode('utf-8')

        clients[client_socket] = name
        print(f'Cliente {name} ({client_address[1]}) conectado.')

        # Crear un hilo para manejar las comunicaciones con el cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

start_server()
