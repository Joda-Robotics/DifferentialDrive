# File to handle outgoing communications
# TCP to server for general commands
# UDP directly to robot for camera
# l = login, r = register, o = other

import socket
from time import sleep
import time
import threading

class baseSocket():

    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = "10.0.0.22"
    ADDR = (SERVER, PORT)

    def startConn(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def stopConn(self):
        self.send(self.DISCONNECT_MESSAGE)

    def upOrDown(self):
        return self.t1.is_alive()

    def send(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

    def acceptMsg(self):
        connected = True
        while connected:

            msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.client.recv(msg_length).decode(self.FORMAT)
                time.sleep(.1)
                connected = False
                return msg

class serverSocket(baseSocket):
    def __init__(self):
        super().__init__()

class robotSocket(baseSocket):
    def __init__(self):
        super().__init__()
        self.SERVER = "10.0.0.31"
        self.PORT = 5050
        self.ADDR = (self.SERVER, self.PORT)

    
