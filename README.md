# Socket Chat

Aplicación simple de chat en una terminal implementada en Python, que consta de un servidor y un cliente que se comunican entre sí a través de una red usando sockets.

## Requisitos previos

Antes de ejecutar la aplicación de chat, asegúrate de tener lo siguiente:

- Python instalado.
- Una conexión de red.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/nselar/SocketsChat.git
   ```

2. Cambia al directorio del proyecto:

   ```bash
   cd socket-chat
   ```

3. Instala las dependencias requeridas:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Servidor

1. Abre el archivo `server.py` en un editor de texto.

2. En la función `start_server`, modifica la siguiente línea para especificar la dirección IP y el puerto en el que el servidor debe escuchar:

   ```python
   server_socket.bind(('192.168.1.40', 12345))
   ```

   Reemplaza `'192.168.1.40'` con la dirección IP deseada y `12345` con el número de puerto deseado.

3. Guarda los cambios.

4. Ejecuta el servidor:

   ```bash
   python server.py
   ```

   El servidor se iniciará y esperará conexiones entrantes.

### Cliente

1. Abre el archivo `client.py` en un editor de texto.

2. En la función `start_client`, modifica la siguiente línea para especificar la dirección IP y el puerto del servidor:

   ```python
   client_socket.connect(('192.168.1.40', 12345))
   ```

   Reemplaza `'192.168.1.40'` con la dirección IP del servidor y `12345` con el número de puerto en el que el servidor está escuchando.

3. Guarda los cambios.

4. Ejecuta el cliente:

   ```bash
   python client.py
   ```

   El cliente se conectará al servidor y podrás comenzar a enviar y recibir mensajes.

## Funcionalidades

- Varios clientes pueden conectarse al servidor simultáneamente.
- Los mensajes enviados por un cliente se transmiten a todos los clientes conectados.
- El servidor muestra el nombre y la dirección de cada cliente conectado.

## Notas

- Para salir del cliente o del servidor, presiona `Ctrl + C`.
- Esta es una implementación básica y no incluye manejo de errores ni encriptación. Úsala con fines educativos o como punto de partida para tus propios proyectos.
- Se han actualizado las librerías requeridas en `requirements.txt` para resolver las vulnerabilidades con las que contaba el proyecto.

Siéntete libre de hacer pull requests explicando qué cambiarías y por qué.
