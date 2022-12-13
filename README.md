# League-client-tools

## Features:
- Auto-accept
- Auto-login
- Stores account information
- Provides op.gg information in GUI

## How it works:
1. The auto-accept feature works by getting the (x, y) coordinates from opencv template matching and uses pyautogui to click at the position found by opencv.
2. The auto-login feature uses pywinauto which interfaces with windows and enters keystrokes in control panes.
3. Account information is stored in a local database using sqlite.
4. Uses beautifulsoup to fetch account information from op.gg.
5. GUI built with tkinter.


## Notes:
- If you want to use this program and you're not on Windows, you'll need to use the python file named "keyboard_sim.py" instead of pywinauto.
- The biggest issue currently is that pyautogui.screenshot() only works on the primary monitor. So, if you have more than 1 monitor, make sure the client is on whichever one is set to "primary"

## Todo:
1. Add GUI button to enable user to edit their file path. (to use the program, you need to go into the tkgui.py file and change the path manually)
2. Make a better gui.
3. Fix monitor bug.
