import socket 
import threading
from time import sleep
from databaseHandler import checkUsername, completeReg, grabPass, checkPassMatch
from passwordEncryption import encrypt, checkpas

# Server details
HEADER = 64
PORT = 5050
SERVER = "10.0.0.22"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# Server base information
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

        self.thread = threading.Thread(target=self.statusChecker)
        self.thread.start()
        self.start()

    # Starts server to listen
    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            self.conn, self.addr = self.server.accept()
            self.thread = threading.Thread(target=handleClient, args=(self.conn, self.addr))
            self.thread.name = self.addr
            self.thread.start()

    # Tells server admin current connections
    def statusChecker(self):
        while True:
            sleep(10)
            print("There are currently {} connected human clients".format(len(self.clientSet)))
            print("There are currently {} connected robots".format(len(self.robotSet)))


    # Tracks current human clients
    clientSet = set()
    # Tracks current robots
    robotSet = set() 

# How to handle outside computers
class handleClient(serverStart):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.HEADER = HEADER
        self.FORMAT = FORMAT
        self.DISCONNECT_MESSAGE = DISCONNECT_MESSAGE
        print(f"[NEW CONNECTION] {addr} connected.")
        print(threading.currentThread().getName())
        self.connected = True

        self.acceptMsg()

    # How to send message correctly.
    # Send length then actual message which has been formatted
    def send(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.conn.send(send_length)
        self.conn.send(message)

    # How to handle incoming messages
    def acceptMsg(self):
        while self.connected:
            msg_length = self.conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = self.conn.recv(msg_length).decode(self.FORMAT)

                if msg == self.DISCONNECT_MESSAGE:
                    self.connected = False
                    print(f"[DISCONNECTION] {self.addr} disconnected.")

                    if self.addr in serverStart.clientSet:
                        serverStart.clientSet.discard(self.addr)

                    elif self.addr in serverStart.robotSet:
                        serverStart.robotSet.discard(self.addr)

                elif msg == "client":
                    serverStart.clientSet.add(self.addr)

                elif msg == "robot":
                    serverStart.robotSet.add(self.addr)

                # Handle login/register/other messages differently
                # [request] [data]
                else:
                    self.msgSplit = msg.split(",")

                    self.request = self.msgSplit[0]

                    # REGISTER
                    #[r][Username][Password1][Password2]
                    if self.request == "r":
                        self.Username = self.msgSplit[1]
                        self.Password1 = self.msgSplit[2]
                        self.Password2 = self.msgSplit[3]

                        #check passwords match
                        if checkPassMatch(self.Password1, self.Password2):
                            print("passwords match")
                            self.send("Passwords match")
                        
                            #check username
                            if checkUsername(self.Username):
                                print("Username already taken")
                                self.send("Username already taken")

                            if checkUsername(self.Username) == False:
                                print("Username not taken")
                                self.send("Username not taken")
                                #encrypt password
                                self.PasswordEnc = encrypt(self.Password1)

                                #put into db
                                print("[SUCCESSFUL REGISTRATION]")
                                completeReg(self.Username,self.PasswordEnc)
                                self.send("[SUCCESSFUL REGISTRATION]")

                        else:
                            print("password don't match")
                            self.send("Passwords don't match")
                    
                    # LOGIN
                    # [l][Username][Password1]
                    if self.request == "l":
                        self.Username = self.msgSplit[1]
                        self.Password1 = self.msgSplit[2]

                        if checkUsername(self.Username):

                            #find matching password for username
                            self.grabbed = grabPass(self.Username)

                            #check password encryption matches, encode both
                            self.Password1 = self.Password1.encode()
                            self.grabbed = self.grabbed.encode()

                            if checkpas(self.Password1, self.grabbed):
                                #allow access
                                print("[SUCCESSFUL LOGIN] - Correct details")

                                self.send("[SUCCESSFUL LOGIN] - Correct details")
                                self.send(self.Username)
                            else:
                                self.send("wrong password")
                                print("wrong password")

                        else: 
                            print("wrong username")
                            self.send("wrong username")

                    # OTHER
                    #[o][data]
                    if self.request == "o":
                        pass

