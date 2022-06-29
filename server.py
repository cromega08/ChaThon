from _thread import *
import asyncio
from select import select
import socket
import sys
import random

class stream:
    def __init__(self, host = socket.gethostbyname(socket.gethostname()), port = None) -> None:
        try:
            self.stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.host = host
            self.port = port if port != None else self.get_avaible()
            self.clients = []
        except: print("An error ocurred with socket creation")

    def create_server(self, num_clients: int) -> None:
        try:
            self.stream.bind((self.host, self.port))
            self.stream.listen(int(num_clients) + 1)
            self_created = False
            while True:
                connection, client = self.stream.accept()
                self.clients.append(connection)
                start_new_thread(self.each_client, (connection, client[0]))
                self.send_message(bytes(f"[{client[0]}] connected", "utf-8"), connection)
                if not self_created: start_new_thread(self.self_client(self.port))
                self_created = True
        finally:
            connection.close()
            self.stream.close()

    def each_client(self, connection:socket.socket, client:str) -> None:

        connection.sendall(bytes(f"Your connection with: {socket.gethostbyname(socket.gethostname())} was successful", "utf-8"))
        
        while True:
            try:
                message = connection.recv(2022)
                if message:
                    to_send = f"[{client}]: {message}"
                    print(to_send); self.send_message(bytes(message, "utf-8"), connection)
            except: continue
    
    def send_message(self, message:bytes, connection:socket.socket) -> None:
        for client in self.clients:
            if client != connection:
                try: client.sendall(message)
                except: client.close(); self.clients.remove(client)

    def create_client(self) -> None:
        try:
            self.stream.connect((self.host, self.port))
            while True:
                sockets_list = [sys.stdin, self.stream]
                read_sockets, write_sockets, error_sockets = select(sockets_list, [], [])
                for sockets in read_sockets:
                    if sockets == self.stream: print(sockets.recv(2022))
                    else:
                        message = input("[You]: ")
                        self.stream.sendall(bytes(message, "utf-8"))
                        print("\n")
        finally: self.stream.close()

    def self_client(self) -> None:
        try:
            self_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self_client.connect((self.host, self.port))
            while True:
                sockets_list = [sys.stdin, self_client] 
                read_sockets, write_sockets, error_sockets = select(sockets_list, [], [])
                for sockets in read_sockets:
                    if sockets == self_client: print(sockets.recv(2022))
                    else:
                        message = input("[You]: ")
                        self_client.sendall(bytes(message, "utf-8"))
                        print("\n")
        finally: self_client.close()
        
    def get_avaible(self) -> int:

        port_n = random.randint(1, 65535)
        try:
            stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            stream.connect(("localhost", port_n))
            connected = True
            port_n += 1
        except:
            connected = False
        finally:
            stream.close()
            return port_n if not connected else self.get_avaible()