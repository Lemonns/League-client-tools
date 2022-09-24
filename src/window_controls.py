from pywinauto.application import Application
import time
import os

#riot.RiotClientMain.print_control_identifiers()
#if "RiotClientServices.exe" in (i.name() for i in psutil.process_iter()):
#    print("True")
#else:
#    print("False")

class WindowController:
    def __init__(self, file_location: str) -> None:
        self.location = file_location
    
    def user_login(self, username, password):
        try:
            riot = Application(backend='uia').start(self.location).connect(title='Riot Client Main', timeout=100)
            riot.RiotClientMain.set_focus()
        
            time.sleep(1)
            riot.RiotClientMain['Pane'].type_keys(f'{username}')
            riot.RiotClientMain['Pane'].type_keys('{TAB}')
            riot.RiotClientMain['Pane'].type_keys(f'{password}')
            riot.RiotClientMain['Pane'].type_keys('{ENTER}')

        except Exception:
            print("Already Logged in")
            return

        else:
            return

    #write a function to close the client and restart it if it's already open        
    def user_logout(self):
        riot = Application(backend='uia').connect(title='Riot Client Main', timeout=100)
        riot.RiotClientMain["Menu"].invoke()
        riot.RiotClientMain["MenuItem5"].invoke()

#def auto_accept():

    """
    League of Legends application 
    MUST be RUNNING for this function 
    to work properly.
    """

    #alternate option for auto accepting
    #while True:
    #    print("Attempting to connect");
    #    try:
    #        lol = Application(backend='uia').connect(title='League of Legends', timeout=100)
    #        lol.LeagueofLegends['ACCEPT!'].invoke()
    #    except Exception:
    #        print("Waiting...")
    #    else:
    #        print("Accepted! Exiting auto-accept...")
    #        return


#auto_accept()


        
        
#main_widow = WindowController("D:\Riot Games\Riot Client\RiotClientServices.exe")
#main_widow.user_login()
#main_widow.user_logout()

