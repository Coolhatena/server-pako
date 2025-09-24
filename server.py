""" Server de Echo """
import socket
import os

# Definir host y puerto
HOST = "192.168.0.114" 
PORT = 65432

path = "/zistemas/"

def list_files(path):
        try:
                entries = os.listdir(path)
                files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]
                return ", ".join(files)
        except FileNotFoundError:
                return f"Error: Directory '{path}' not found."
        except Exception as e:
                return f"An error occurred: {e}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
                s.listen()
                print(f"Servidor escuchando en {HOST}:{PORT}")
                conn, addr = s.accept()
                with conn:
                        print(f"Conectado por {addr}")
                        while True:
                                data = conn.recv(1024)
                                if not data:
                                        break

                                response = ""
                                data = data.decode("utf-8")
                                tokens = data.split(" ")
                                main_command = tokens[0]
                                match main_command:
                                        case "ls":
                                                print("Comando recibido: Listar")
                                                received_path = tokens[1] if len(tokens) > 1 else ""
                                                print(f"Ruta solicitada: {received_path}")
                                                response += f"Archivos en {path}{received_path}: \n"
                                                response += list_files(path + received_path)
                                        case "get":
                                                print("Comando recibido: Obtener")
                                                received_path = tokens[1] if len(tokens) > 1 else ""
                                                print(f"Ruta solicitada: {received_path}")
                                                response += f"Contenido del archivo {received_path}\n"
                                                with open(path + received_path) as f: response += f.read()
                                        case _:
                                                response += f"Comando desconocido: {main_command}"

                                conn.sendall(response.encode("utf-8"))
