import numpy as np
import cv2
import pyautogui
import time
import multiprocessing

THRESHHOLD = 0.9
searching = True

#This script can only be used on primary monitor
#pyautogui has issues with this
class Auto:
    def __init__(self) -> None:
        self.process = multiprocessing.Process(target=self.find_accept_btn, args=())

    
    def find_accept_btn(self):
        #continuously searches for accept button
        while searching:
            img_bgr = pyautogui.screenshot()
            img_bgr = cv2.cvtColor(np.array(img_bgr), cv2.COLOR_RGB2BGR)
            img_bgr = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
            template = cv2.imread('./images/accept-template.png', 0)

            w ,h = template.shape[::-1]
            res = cv2.matchTemplate(img_bgr, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= THRESHHOLD)

            time.sleep(1)
            print("Searching...  (Press 'Quit' to quit)")

            if loc[0].any():
                #searching = False

                #location of found button
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) 
                print(f"Found at {max_loc}")

                for pt in zip(*loc[::-1]):
                    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (255, 1, 255), 2)
                pyautogui.click(max_loc[0]+2, max_loc[1])
                time.sleep(2)

    #starts process of find_accept_btn()
    def gui_compatable(self):
        self.process.start()

    #ends process of find_accept_btn()
    def gui_quit(self):
        self.process.terminate()
        print("Stopped")
        self.process = multiprocessing.Process(target=self.find_accept_btn, args=())


#t1 = Thread(target = find_accept_btn)
#t1.start()
#cv2.imshow('detected', img_bgr)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

