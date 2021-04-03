#main file to launch client

import kivy
from kivy.app import App
# kivy.require helps with version compatibility 
kivy.require('1.11.1')
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.properties import *
from communications import serverSocket
from communications import robotSocket


# Class to hold socket instances to share between windows
class connectionToServer():
    def beginConn(self):
        self.serverInstance = serverSocket()
        self.serverInstance.startConn()

    def stopConnect(self):
        self.serverInstance.stopConn()

class WindowManager(ScreenManager):
    pass

class LoginWindow(Screen):

    loginUsername = ObjectProperty(None)
    loginPassword = ObjectProperty(None)

    def reset(self):
        self.loginUsername.text = ""
        self.loginPassword.text = ""

    def login(self):
        self.allowAccess = 0
        yy.beginConn()
        yy.serverInstance.send("client")

        # Send message
        yy.msg = ("l" + "," + self.loginUsername.text.capitalize() + "," + self.loginPassword.text)
        yy.serverInstance.send(yy.msg)

        # Accept return message
        yy.returnedMessage = yy.serverInstance.acceptMsg()
        print(yy.returnedMessage)
        if yy.returnedMessage == "[SUCCESSFUL LOGIN] - Correct details":
            self.allowAccess = 1
        else:
            yy.stopConnect()

class RegisterWindow(Screen):

    registerDesiredUsername = ObjectProperty(None)
    registerPassword1 = ObjectProperty(None)
    registerPassword2 = ObjectProperty(None)

    def beginConn(self):
        self.serverInstance = serverSocket()
        self.serverInstance.startConn()

    def stopConnect(self):
        self.serverInstance.stopConn()

    def resetAll(self):
        self.registerDesiredUsername.text = ""
        self.registerPassword1.text = ""
        self.registerPassword2.text = ""

    def resetPasswords(self):
        self.registerPassword1.text = ""
        self.registerPassword2.text = ""

    def register(self):
        # Create conn
        self.serverInstance = serverSocket()
        self.serverInstance.startConn()
        self.allowReg = 0

        # Send message
        self.msg = ("r" + "," + self.registerDesiredUsername.text.capitalize() + "," + self.registerPassword1.text + "," + self.registerPassword2.text)
        self.serverInstance.send(self.msg)

        # Accept return message
        self.returnedMessage = self.serverInstance.acceptMsg()

        # Check password match
        if self.returnedMessage == "Passwords don't match":
            print("Passwords don't match")
            self.resetPasswords()
            self.serverInstance.stopConn()

        elif self.returnedMessage == "Passwords match":
            print("Passwords match")
            self.returnedMessage = self.serverInstance.acceptMsg()

            # Check username availablity
            if self.returnedMessage == "Username already taken":
                print("Username already taken")
                self.resetAll()
                self.serverInstance.stopConn()

            elif self.returnedMessage == "Username not taken":
                print("Username not taken")

                # New message to confirm rego
                self.returnedMessage = self.serverInstance.acceptMsg()

                if self.returnedMessage == "[SUCCESSFUL REGISTRATION]":
                    print("Successful")
                    self.serverInstance.stopConn()
                    self.allowReg = 1


class MainWindow(Screen):
    useName = StringProperty("None")

    def getUserLabel(self):
        if self.useName == "None":
            yy.returnedMessage = yy.serverInstance.acceptMsg()
            self.useName = "Hello " + yy.returnedMessage

    def endSession(self):
        print("bye")
        yy.stopConnect()

class RobotOneWindow(Screen):

    def robotServerInstanceStart(self):
        self.robotInstance = robotSocket()
        self.robotInstance.startConn()

    def robotServerInstanceStop(self):
        self.robotInstance.stopConn()

    def moveF(self):
        self.msg = ("w")
        self.robotInstance.send(self.msg)

    def moveB(self):
        self.msg = ("s")
        self.robotInstance.send(self.msg)

    def moveR(self):
        self.msg = ("d")
        self.robotInstance.send(self.msg)

    def moveL(self):
        self.msg = ("a")
        self.robotInstance.send(self.msg)

    def moveStop(self):
        self.msg = ("z")
        self.robotInstance.send(self.msg)

    def testP(self):
        self.msg = ("p")
        self.robotInstance.send(self.msg)

        self.returnedMessage = self.robotInstance.acceptMsg()
        print(self.returnedMessage)

    def getUSDistanceF(self):
        self.msg = ("USD")
        self.robotInstance.send(self.msg)
        print("hel")

        self.returnedMessage = self.robotInstance.acceptMsg()
        print(self.returnedMessage)

    def getUSDistanceB(self):
        pass

    def currentSpeed(self):
        pass


kv = Builder.load_file("main.kv")

# Object of class to hold global server connection
yy = connectionToServer()

class JodaClientApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    JodaClientApp().run()