#     <ChaThon: A CLI Chat Application>
#     Copyright (C) <2022>  <Cromega>

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from _thread import *
from select import select
import socket
import subprocess
import sys
import random

class stream:
    
    def __init__(self, host = socket.gethostbyname(socket.gethostname()), port = None) -> None:
        
        try:
            
            self.stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.host = host
            self.port = port if port != None else self.get_avaible()
        
        except: print("An error ocurred with socket creation")

    def create_server(self, num_clients: int) -> None:
        
        try:

            print(self.host, self.port, sep="\n", end="\n")

            self.stream.bind((self.host, self.port))
            self.stream.listen(int(num_clients) + 1)
            self.i = False
            self_created = False
            self.clients = []
            self.close = False
            
            while True:

                if self.close: break

                connection, client = self.stream.accept()
                self.clients.append(connection)
                start_new_thread(self.each_client, (connection, client[0]))
                self.send_message(bytes(f"[{client[0]}] connected to the server", "utf-8"), connection)
                
                if not self_created: start_new_thread(self.self_client, ()); self_created = True
        
        finally:
            
            self.stream.close()

    def each_client(self, connection:socket.socket, client:str) -> None:

        connection.sendall(bytes(f"\nYour connection with: {socket.gethostbyname(socket.gethostname())} was successful", "utf-8"))
        
        while True:
            
            try:
                
                message = connection.recv(2022)
                
                if message != b"":
                    
                    to_send = f"[{client}]: {message.decode('utf-8')}"
                    self.send_message(bytes(to_send, "utf-8"), connection)
                
                else: self.clients.remove(connection); connection.close(); break
            
            except: continue

        if len(self.clients) == 0: self.kill()

    def send_message(self, message:bytes, connection:socket.socket) -> None:
        
        for client in self.clients:
            
            if client != connection or self.i == True:
                
                try: client.sendall(message)
                
                except: client.close(); self.clients.remove(client)

    def create_client(self) -> None:

        try:

            self.stream.connect((self.host, self.port))

            while True:

                sockets_list = [sys.stdin, self.stream]
                read_sockets, write_sockets, error_sockets = select(sockets_list, [], [])
                
                for sockets in read_sockets:
                    
                    if sockets == self.stream:
                        
                        message = sockets.recv(2022)
                        
                        if message == b"": break
                        
                        print(f"{message.decode('utf-8')}\n")
                    
                    else:
                        
                        message = input("-> ")
                        self.stream.sendall(bytes(message, "utf-8"))
                
                if message == b"": break

        finally: self.stream.close(); print(f"Connection with {self.host} was finished"); sys.exit()

    def self_client(self) -> None:

        self.i = True
        subprocess.call(["xterm", "-e", f"chathon c -ip {self.host} -p {self.port}"])
        
    def get_avaible(self) -> int:

        port_n = random.randint(1, 65535)

        try:

            stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            stream.connect(("localhost", port_n))
            connected = True
            port_n += 1

        except: connected = False
        
        finally:
            
            stream.close()
            return port_n if not connected else self.get_avaible()
    
    def kill(self) -> None:

        self.close = True; self.self_client()
