from guizero import *

mainWin = App(title = "Joda Robotics Systems", width=800, height=800, layout="grid")

def startRobot1Manual():
    robot1AutoButton.enable()
    robot1ManualButton.disable()
    robot1Window = Window(mainWin, bg="red", title="Robot 1 control view!!!")
    robot1StatusText = Text(robot1Box, grid=[1,0], text="MANUAL CONTROL YEWWWW!")
    
def startRobot2Manual():
    robot2AutoButton.enable()
    robot2ManualButton.disable()

def startRobot3Manual():
    robot3AutoButton.enable()
    robot3ManualButton.disable()

def startRobot1Auto():
    robot1AutoButton.disable()
    robot1ManualButton.enable()

def startRobot2Auto():
    robot2AutoButton.disable()
    robot2ManualButton.enable()

def startRobot3Auto():
    robot3AutoButton.disable()
    robot3ManualButton.enable()
    
def destroyAll():
    mainWin.destroy()


jodaImageBox = Box(mainWin, border=4, width=800, height=80, grid=[0,0])
robotMenuBox = Box(mainWin, width=800, height=80, grid=[0,2], border=0, layout="grid")
overallStatusBox = Box(mainWin, width = 500, height=40, grid=[0,1])

robotMenuBoxName = Box(robotMenuBox, width=199, height=70, border=1, grid=[0,0])
robotMenuBoxStatus = Box(robotMenuBox, width=199, height=70, border=1, grid=[1,0])
robotMenuBoxManual = Box(robotMenuBox, width=199, height=70, border=1, grid=[2,0])
robotMenuBoxAuto = Box(robotMenuBox, width=199, height=70, border=1, grid=[3,0])

robotClumpBox = Box(mainWin, width=800, height=600, grid=[0,3], layout="grid",)

robot1Box = Box(robotClumpBox, grid=[0,0], layout="grid", width=199, height=70, border=1)
robot2Box = Box(robotClumpBox, grid=[0,1], layout="grid", width=199, height=70, border=1)
robot3Box = Box(robotClumpBox, grid=[0,2], layout="grid", width=199, height=70, border=1)
destroyBox = Box(robotClumpBox, grid=[0,3], width=199, height=70, border=1)

robot1NameText = Text(robot1Box, grid=[0,0], text="Robot 1")
robot2NameText = Text(robot2Box, grid=[0,0], text="Robot 2")
robot3NameText = Text(robot3Box, grid=[0,0], text="Robot 3")

robot1StatusText = Text(robot1Box, grid=[1,0], text="OK!")
robot2StatusText = Text(robot2Box, grid=[1,0], text="OK!")
robot3StatusText = Text(robot3Box, grid=[1,0], text="OK!")

robot1ManualButton = PushButton(robot1Box, text="MANUAL CONTROL", grid=[2,0], command=startRobot1Manual)
robot2ManualButton = PushButton(robot2Box, text="MANUAL CONTROL", grid=[2,0], command=startRobot2Manual)
robot3ManualButton = PushButton(robot3Box, text="MANUAL CONTROL", grid=[2,0], command=startRobot3Manual)

robot1AutoButton = PushButton(robot1Box, text="AUTO CONTROL", grid=[3,0] ,enabled=False, command=startRobot1Auto)
robot2AutoButton = PushButton(robot2Box, text="AUTO CONTROL", grid=[3,0] ,enabled=False, command=startRobot2Auto)
robot3AutoButton = PushButton(robot3Box, text="AUTO CONTROL", grid=[3,0] ,enabled=False, command=startRobot3Auto)

destroyAllButton = PushButton(destroyBox, text="Quit all", command=destroyAll)


textMainImage = Text(jodaImageBox, text = "Joda picture goes here", size = 20)

textMenuName = Text(robotMenuBoxName, text = "Name of robot")
textMenuStatus = Text(robotMenuBoxStatus, text = "Status")
textMenuManual = Text(robotMenuBoxManual, text = "Press for manual")
textMenuAuto = Text(robotMenuBoxAuto, text = "Press for auto")

textOverallStatus = Text(overallStatusBox, text = "All is ok!", size = 20)



mainWin.display()