import pyautogui as peg
import time

time.sleep(4)
count = 1

while count <= 20:
    peg.typewrite("Yo Mama" + str(count))
    peg.press("enter")
    count = count + 1
