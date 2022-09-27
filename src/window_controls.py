from pywinauto.application import Application
import time
import os
import psutil
import subprocess

#riot.RiotClientMain.print_control_identifiers()


#Controls automated login functionality
#Window controller needs path of client to work
class WindowController:
    def __init__(self, file_location: str) -> None:
        self.location = file_location
    
    def user_login(self, username, password):
        try:
            updating = True

            #If client is running, kills all instances of riot and league client 
            if "RiotClientServices.exe" in (i.name() for i in psutil.process_iter()):
                subprocess.call("TASKKILL /F /IM RiotClientServices.exe")
                subprocess.call("TASKKILL /F /IM LeagueClient.exe")
                subprocess.call("TASKKILL /F /IM LeagueClientUx.exe")
                subprocess.call("TASKKILL /F /IM LeagueClientUxRender.exe")
                print("True")
                
            riot = Application(backend='uia').start(self.location).connect(title='Riot Client Main', timeout=100)
            riot.RiotClientMain.set_focus()
        
            time.sleep(1)
            riot.RiotClientMain['Pane'].type_keys(f'{username}')
            riot.RiotClientMain['Pane'].type_keys('{TAB}')
            riot.RiotClientMain['Pane'].type_keys(f'{password}')
            riot.RiotClientMain['Pane'].type_keys('{ENTER}')
            
            time.sleep(1)

            #Automatically clicks the league of legends icon under "Games"
            riot.RiotClientMain["League of Legends"].invoke()
            #riot.RiotClientMain["Valorant"].invoke()  <-- For when Valorant support is added
            while updating:

                #Exits loop if game is NOT updating
                try:
                    time.sleep(1)
                    riot.RiotClientMain["Play"].invoke()
                    print("Not updating")
                    updating = False
                    break
                
                #Continues loop if game is updating
                except Exception:
                    time.sleep(15)
                    print("Updating...")
                    continue

        except Exception:
            print(f"Error: {Exception}")
            return

        else:
            return

    #Logs out of the riot client. Useless as of now
    def user_logout(self):
        riot = Application(backend='uia').connect(title='Riot Client Main', timeout=100)
        riot.RiotClientMain["Menu"].invoke()
        riot.RiotClientMain["MenuItem5"].invoke()


    #This function can be used instead of the opencv script, but it is much slower and can only run on windows
    def auto_accept(self):
        """
        League of Legends application 
        MUST be RUNNING for this function 
        to work properly.
        """
        while True:
            print("Attempting to connect");
            try:
                lol = Application(backend='uia').connect(title='League of Legends', timeout=100)
                lol.LeagueofLegends['ACCEPT!'].invoke()
            except Exception:
                print("Waiting...")
            else:
                print("Accepted! Exiting auto-accept...")
                return