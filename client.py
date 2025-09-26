"""cliente de eko"""
import socket
# Definimos el host y el puerto
HOST = "192.168.0.114" # La misma direccion del servidor
PORT = 65432 # El mismo puerto del servicio
# Creamos el objeto de socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Conectamos el socket a la direccion y el puerto del servidor
        s.connect((HOST, PORT))
        print(f"Conectando al servidor en {HOST}:{PORT}")
        
        data = s.recv(1024)
        print(f"Server: {data.decode('utf-8')}")
        
        while True:
            # Mensaje que queremos enviar al servidor
            message = input(">: ")
            # Enviamos el mensaje codificado
            s.sendall(message.encode("utf-8"))
            print(f"Enviado: {message}")

            # Recibimos los datos de respuesta del servidor
            data = s.recv(1024)
            print(f"Recibido: {data.decode('utf-8')}")

