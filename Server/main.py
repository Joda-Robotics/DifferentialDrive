# Main server file

from time import sleep
import threading
import communications

# Create server

def startServer():
    serverInstance = communications.serverStart()

if __name__ == "__main__":
    startServer()