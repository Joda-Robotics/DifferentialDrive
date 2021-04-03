from picamera import *
from guizero import *
from gpiozero import *
from enum import Enum
from io import BytesIO
from time import sleep
from PIL import *

stream = BytesIO()
camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 180
#camera.start_preview()
'''sleep(2)
camera.capture(stream, format='jpeg')
stream.seek(0)
image = Image.open(stream)'''
#camera.end_preview()

def startEng():
    print("started!")
    startBut.disable()
    stopBut.enable()
    engStatusG.rectangle(10, 10, 50, 50, color="green")
    engStatusR.clear()
    
def stopEng():
    print("stopped!")
    startBut.enable()
    stopBut.disable()
    engStatusR.rectangle(10, 10, 50, 50, color="red")
    engStatusG.clear()

def goF():
    print("forward!")
    
def goL():
    print("left!")
    
def goR():
    print("right!")
    
def goB():
    print("back!")
    

controlWindow = App(title="Wagon Control", width = 800, height = 950)

openMsg = Text(controlWindow, text="Let's control this robot.")
startBut = PushButton(controlWindow, command=startEng, text="Start engine")
engStatusG = Drawing(controlWindow, width=100, height=50)
engStatusR = Drawing(controlWindow, width=100, height=60)

engStatusR.rectangle(10, 10, 50, 50, color="red")
stopBut = PushButton(controlWindow, command=stopEng, text="Stop engine", enabled=False)
gearText = Text(controlWindow, text="Select gear")
gearChoice = ButtonGroup(controlWindow, options=["one", "two", "three"], selected="one", horizontal='true')
directionBox = Box(controlWindow)
f = PushButton(directionBox, command=goF, align="top", text="go forward")
l = PushButton(directionBox, command=goL, align="left", text="go left")
r = PushButton(directionBox, command=goR, align="right", text="go right")
b = PushButton(directionBox, command=goB, align="bottom", text="go back")
camPretxt = Text(controlWindow, text="Below is camera view")
cameraScuff = Drawing(controlWindow, width = 720, height=480)
cameraScuff.rectangle(40, 40, 820, 820)
controlWindow.display()