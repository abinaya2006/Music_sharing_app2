import socket
from threading import Thread
import os

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

is_dir_exists = os.path.isdir('shared_files')
print(is_dir_exists)
if(not is_dir_exists):
    os.makedirs('shared_files')

def acceptConnections():
    global SERVER
    global clients

    while True:
        client,addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        clients[client_name] = {
            "client" :client,
            "address" : addr,
            "connected_with"  :"",
            "file_name":"",
            "file_size":4096
        }

        print(f"Connection established with {client_name}:{addr}")

        thread =Thread(target=handleClient , args=(client,client_name))
        thread.start()
    

def setup():
    print("\n\n\t\t IP MESSENGER \n")

    global SERVER,IP_ADDRESS,PORT

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(100)

    print("\n\t\tServe is ready to accept connections\n")

    acceptConnections()

setup_target = Thread(target=setup)
setup_target.start()

