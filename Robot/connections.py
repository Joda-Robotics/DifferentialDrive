# File to handle outgoing communications
# TCP to server for general commands
# UDP directly to robot for camera
# l = login, r = register, o = other

import socket
from time import sleep
import threading
from movement import movements
import movement

class baseSocket():
    def __init__(self):
        self.startConn()
        self.send("robot")
        self.thread = threading.Thread(target=self.acceptMsg, daemon=True)
        self.thread.start()
        self.thread = threading.Thread(target=self.directConnection, daemon=True)
        self.thread.start()
        self.countdown()
        

    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = "10.0.0.22"
    ADDR = (SERVER, PORT)

    def directConnection(self):
        directConnection = serverStart()

    def countdown(self):
        sleep(60)
        self.stopConn()

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
                connected = True
                return msg

class serverSocket(baseSocket):
    def __init__(self):
        super().__init__()

# Create own server when asked
# Human client connects to robot server

HEADER = 64
PORT = 5050
SERVER = "10.0.0.31"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

class serverStart():
    def __init__(self):
        self.HEADER = HEADER
        self.PORT = PORT
        self.SERVER = SERVER
        self.ADDR = ADDR
        self.FORMAT = FORMAT
        self.DISCONNECT_MESSAGE = DISCONNECT_MESSAGE
    
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)

        self.start()

    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            self.conn, self.addr = self.server.accept()
            self.thread = threading.Thread(target=handleClient, args=(self.conn, self.addr))
            self.thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

class handleClient(serverStart,movements):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.HEADER = HEADER
        self.FORMAT = FORMAT
        self.DISCONNECT_MESSAGE = DISCONNECT_MESSAGE
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        self.acceptMsg()

    def send(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.conn.send(send_length)
        self.conn.send(message)

    def acceptMsg(self):
        connected = True
        while connected:
            sleep(.1)
            msg_length = self.conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.conn.recv(msg_length).decode(self.FORMAT)

                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
                    print(f"[DISCONNECTION] {self.addr} disconnected.")

                if msg == "w":
                    movements().forwardDrive()

                if msg == "s":
                    movements().reverseDrive()

                if msg == "d":
                    movements().spinRight()

                if msg == "a":
                    movements().spinLeft()

                if msg == "z":
                    movements().allStop()

                if msg == "p":
                    print("pepe")
                    self.send("pepe")

                if msg == "USD":
                    print("USD")
                    self.send("1")
