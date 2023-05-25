import socket
import threading

def receive_messages(client_socket):
    while True:
        # Esperar a recibir datos del servidor
        data = client_socket.recv(1024).decode('utf-8')
        print(data)

def start_client():
    # Configurar el socket del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.40', 12345))
    print('Conectado al servidor.')

    # Crear un hilo para recibir mensajes del servidor
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        # Leer los mensajes del usuario y enviarlos al servidor
        message = input()
        client_socket.send(message.encode('utf-8'))

start_client()