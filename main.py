'''
- Spawns main GUI and performs initial configuration
- Creates model (the model creates the system state and an interface to control the robot)
'''


import createMainGUI 


def main():
    
    createMainGUI.mainGUIApp().run()


if __name__ == "__main__":
    main()