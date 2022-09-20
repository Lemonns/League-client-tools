from subprocess import Popen, PIPE
from pynput.keyboard import Key, Controller
import time

class Commands():

    def __init__(self, file_location):
        self.keyboard = Controller()
        self.location = file_location
        self.opener = Popen([self.location],stdin=PIPE,stdout=PIPE,stderr=PIPE, encoding="UTF8")

    def enter_information(self):
        time.sleep(5)
        self.keyboard.type("Username")
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
        self.keyboard.type("Password")
        self.keyboard.release(Key.tab)
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)


main_controller = Commands("D:\Riot Games\Riot Client\RiotClientServices.exe")
main_controller.enter_information()