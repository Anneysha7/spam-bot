import pyautogui
import time

time.sleep(3)

# print(pyautogui.size())

# time.sleep(3)
# print(pyautogui.position())
# time.sleep(3)
# print(pyautogui.position())

distance = 300

while (distance>0):
    pyautogui.dragRel(distance, 0, 1, button='left')
    distance-=20
    pyautogui.dragRel(0, distance, 1, button='left')
    pyautogui.dragRel(-distance, 0, 1, button='left')
    distance-=20
    pyautogui.dragRel(0, -distance, 1, button='left')

# pyautogui.mouseDown(100, 200, button='left')
# pyautogui.moveTo(800, 200)
# pyautogui.moveTo(800, 900)
# pyautogui.moveTo(100, 900)
# pyautogui.moveTo(100, 300)
# pyautogui.moveTo(700, 300)
# pyautogui.moveTo(700, 800)
# pyautogui.moveTo(200, 800)
# pyautogui.moveTo(200, 400)
# pyautogui.moveTo(600, 400)
# pyautogui.moveTo(600, 700)
# pyautogui.moveTo(300, 700)
# pyautogui.moveTo(300, 500)
# pyautogui.mouseUp()
