import subprocess

subprocess.call("TASKKILL /F /IM RiotClientServices.exe")
subprocess.call("TASKKILL /F /IM LeagueClient.exe")
subprocess.call("TASKKILL /F /IM LeagueClientUx.exe")
subprocess.call("TASKKILL /F /IM LeagueClientUxRender.exe")