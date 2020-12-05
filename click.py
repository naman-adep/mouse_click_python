import pyautogui, sys, time

pyautogui.FAILSAFE = True
pyautogui.click(x=23, y=1052)  # move to 100, 200, then click the left mouse button.
time.sleep(4)
pyautogui.click(button='right')  # right-click the mouse
time.sleep(4)
pyautogui.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
time.sleep(4)
pyautogui.doubleClick()  # perform a left-button double click