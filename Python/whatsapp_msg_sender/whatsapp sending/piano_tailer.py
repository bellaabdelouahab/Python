#import os, sys
from PIL import ImageGrab

import pyautogui
def screenGrab():
    im = ImageGrab.grab((345,393,631,508))
    if im.getpixel((50,45+20))==(2,2,2):
        pyautogui.click(45+345,393+150)
    elif im.getpixel((120,70))==(2,2,2):
        pyautogui.click(120+345,393+150)
    elif im.getpixel((180,70))==(2,2,2):
        pyautogui.click(180+345,393+150)
    elif im.getpixel((240,70))==(2,2,2):
        pyautogui.click(240+345,393+150)
    #im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) +'.png', 'PNG')
while True:
    screenGrab()

