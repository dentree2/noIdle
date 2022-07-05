import pyautogui
import time
from datetime import datetime
print("Script is running... Press CTRL+C in the console to quit.")
while True:
    firstMousePos = pyautogui.position()
    time.sleep(180)
    secondMousePos = pyautogui.position()
    if firstMousePos == secondMousePos:
        print("No motion:", secondMousePos, " at {}".format(datetime.now().time()))
        pyautogui.moveTo(40, 40)
        for i in range(40, 80):
            pyautogui.moveTo(i * 5, i * 10)
        # pyautogui.click()
        pyautogui.press("shift")
    else:
        print("Motion:   ", secondMousePos, " at {}".format(datetime.now().time()))
