# Main robot file
# Connect to server first
# Accept server commands or accept new connection from a human client

from connections import serverSocket
from movement import movements

# Starts connection to server
def startRobotServerConnection():
    robotInstance = serverSocket()

if __name__ == "__main__":
    startRobotServerConnection()