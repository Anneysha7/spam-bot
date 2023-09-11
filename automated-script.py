# automated text messaging

#import
import time
import pyautogui

def SendMessage():
    time.sleep(4)
    text = open('F:/spam-bot/message.txt')
    for line in text:
        pyautogui.typewrite(line)
        pyautogui.press('enter')


SendMessage()
