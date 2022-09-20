from bs4 import BeautifulSoup
from window_controls import WindowController

p = WindowController("D:\Riot Games\Riot Client\RiotClientServices.exe")
p.user_login()


#we should probably use the riot api here