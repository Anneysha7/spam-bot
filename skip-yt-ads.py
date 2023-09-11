import pyautogui
import time

def get_timer_status():               # gets timer status
    return 0

# track the location of the skip ads panel
x = 0                                 # gets central x coordinate
y = 0                                 # gets central y coordinate

# checks type of panel (timer, skip button and actions accordingly)
timer = get_timer_status()            # timer state (0: absent, 1: present)
dur = 0                               # timer duration
while timer == 1:
    time.sleep(dur)
    timer = get_timer_status()
    if timer == 0:
        pyautogui.click(x, y)
        timer = get_timer_status()   
