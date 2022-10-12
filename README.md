# League-client-tools

## Features:
- Auto-accept
- Auto-login
- Stores account information
- Provides op.gg information in GUI

## How it works:
1. The auto-accept feature works by getting the (x, y) coordinates from opencv template matching and uses pyautogui to click at the (x, y) position.
2. The auto-login feature uses pywinauto which interfaces with windows and enters keystrokes in control panes.
3. Account information is stored in a local database using sqlite.
4. Uses beautifulsoup to fetch account information from op.gg.
5. GUI built with tkinter.

## Notes:
  As of now this program only works on windows. It uses pywinauto for the auto-login feature which, hence the name, only works on windows. You could use another library pynput or something to automate keystrokes, but if you click off of the window while the client is booting up, your keystrokes would go elsewhere. Other than that, I think everything else would work pretty well. 
