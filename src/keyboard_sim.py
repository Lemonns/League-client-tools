from subprocess import *
import subprocess
import psutil
from pynput.keyboard import Key, Controller
import time

class Commands():

    def __init__(self, file_location):
        self.keyboard = Controller()
        self.location = file_location
        #self.open = Popen([self.location],stdin=PIPE,stdout=PIPE,stderr=PIPE, encoding="UTF8")

    def enter_information(self):
        #If client already open, close it
        if "RiotClientServices.exe" in (i.name() for i in psutil.process_iter()):
            subprocess.call("TASKKILL /F /IM RiotClientServices.exe")
            subprocess.call("TASKKILL /F /IM LeagueClient.exe")
            subprocess.call("TASKKILL /F /IM LeagueClientUx.exe")
            subprocess.call("TASKKILL /F /IM LeagueClientUxRender.exe")
            time.sleep(2)
            
        Popen([self.location],stdin=PIPE,stdout=PIPE,stderr=PIPE, encoding="UTF8")   
        time.sleep(5)
        self.keyboard.type("Username")
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
        self.keyboard.type("Password")
        self.keyboard.release(Key.tab)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
