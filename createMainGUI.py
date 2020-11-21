'''
Create GUI for easier way to interact with robots and system
'''

import kivy
# kivy.require helps with version compatibility 
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget



class HomeWindow(Screen):
    pass

class SystemWindow(Screen):
    pass

class RobotListWindow(Screen):
    pass

class RobotControlWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class mainGUIApp(App):
    pass


