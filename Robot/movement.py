from gpiozero import *
from time import *

class movements():

    PWMDriveLeft = 13
    ForwardLeftPin = 19
    ReverseLeftPin = 26

    PWMDriveRight = 12
    ForwardRightPin = 21
    ReverseRightPin = 20

    driveLeft = PWMOutputDevice(PWMDriveLeft, True, 0, 1000)
    driveRight = PWMOutputDevice(PWMDriveRight, True, 0, 1000)

    forwardLeft = PWMOutputDevice(ForwardLeftPin)
    reverseLeft = PWMOutputDevice(ReverseLeftPin)
    forwardRight = PWMOutputDevice(ForwardRightPin)
    reverseRight = PWMOutputDevice(ReverseRightPin)

    def allStop(self):
        self.forwardLeft.value = False
        self.reverseLeft.value = False
        self.forwardRight.value = False
        self.reverseRight.value = False
        self.driveLeft.value = 0
        self.driveRight.value = 0
        
    def forwardDrive(self):
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 1
        self.driveRight.value = 1
        
    def reverseDrive(self):
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 1
        self.driveRight.value = 1
        
    def spinLeft(self):
        self.forwardLeft.value = False
        self.reverseLeft.value = True
        self.forwardRight.value = True
        self.reverseRight.value = False
        self.driveLeft.value = 1
        self.driveRight.value = 1
        
    def spinRight(self):
        self.forwardLeft.value = True
        self.reverseLeft.value = False
        self.forwardRight.value = False
        self.reverseRight.value = True
        self.driveLeft.value = 1
        self.driveRight.value = 1
        
