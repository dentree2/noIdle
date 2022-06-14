# noIdle
A simple script to prevent a remote session from logging an idle status due to user inactivity. The intent of this program is to bring some relief through the natural flow of productivity cycles. 

### Installation 
1. Install [Python](https://www.python.org/downloads/)
2. Install [pyautogui](https://pyautogui.readthedocs.io/en/latest/install.html) 
	- On Windows, type `pip install pyautogui` in the Command Prompt console. 
	- On Mac or Linux, type `pip3 install pyautogui` in the Terminal.
3. Using the Command Prompt or Terminal, navigate to the directory where `noIdle.py` is installed. Use `python noIdle.py` to run the program.

### Full Code Block:

```python
import pyautogui
import time
from datetime import datetime

print("Script is running... Press CTRL+C in the console to quit.")
while(True): 
    firstMousePos = pyautogui.position()
    time.sleep(180)
    secondMousePos = pyautogui.position()
    if firstMousePos == secondMousePos: 
        print("No motion:", secondMousePos, " at {}".format(datetime.now().time()))
        pyautogui.moveTo(40,40)
        for i in range(40,80):
            pyautogui.moveTo(i*5,i*10)
        pyautogui.press("shift")
    else:
        print("Motion:   ", secondMousePos, " at {}".format(datetime.now().time()))
```

### Theory Overview
This program prevents the system from going idle from user inactivity. This can bypass user status indicators through systems like Skype and Microsoft Teams which change to *Away* after 5 minutes of inactivity. 

**Dependencies:** 
 - pyautogui : allows the program to read and manipulate the cursor position
 - time : allows the program to wait for a set duration of system time 
 - datetime : allows the program to print the date/time to the console and log each loop

### Flow 
1. The program prints a message to the console which lets the user know that the script has started and how to exit the loop. 

```python
   print("Script is running... Press CTRL+C in the console to quit.")
```

2. The program begins a continuous loop which stores the cursor position to `firstMousePos` , waits 3 minutes, then stores the cursor position to `secondMousePos`.

```python 
   while(True): 
    firstMousePos = pyautogui.position()
    time.sleep(180)
    secondMousePos = pyautogui.position()
```

3. The program compares the two cursor position variables. If the cursor positions are the same, there has been no cursor movement. The program then moves the cursor and logs the position and time. 

``` python 
   if firstMousePos == secondMousePos: 
        print("No motion:", secondMousePos, " at {}".format(datetime.now().time()))
        pyautogui.moveTo(40,40)
        for i in range(40,80):
            pyautogui.moveTo(i*5,i*10)
        pyautogui.press("shift")
```

4. If the cursor positions are different, there has been cursor movement. The program will log the position and time and take no further action. The user is not interrupted and the loop starts over. 

```python 
   else:
        print("Motion:   ", secondMousePos, " at {}".format(datetime.now().time()))
```

### Sample Output
**Idle Cursor:**
` No motion: Point(x=395, y=790) at 11:53:22.800441 `

**Active Cursor:**
` Motion: Point(x=1073, y=477) at 08:45:54.144668 `

### Considerations
 - If you are using a remote session, and are active on the host PC in a different window (other than the remote session), the remote session may log inactivity during this period of time. 
 - If you plan to step away from the host PC for more than 3 minutes, ensure the remote session window is active (selected) so that it can register cursor movements made by the program. 
 - Depending on the host PC sleep settings, the program may become suspended even when running. 
 - The program moves the cursor to (40,40) and then creates a diagonal line moving downward and rightward. If you need to adjust this setting, change the line `pyautogui.moveTo(40,40)` to the pixel coordinates desired. 
 - The program waits for three minutes between cycles. If you want to change this interval, adjust the line `time.sleep(180)` to the desired duration (in seconds).
