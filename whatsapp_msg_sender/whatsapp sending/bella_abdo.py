#import os, sys
import os
import time
from PIL import ImageGrab

import pyautogui
# def screenGrab():
#     im = ImageGrab.grab((431,88,698,556))
#     if im.getpixel((32,312))==(1,1,1) or im.getpixel((32,312))==(0,2,3):
#         pyautogui.press('d')
#     if im.getpixel((100,312))==(1,1,1) or im.getpixel((100,312))==(0,2,3):
#         pyautogui.press('f')
#     elif im.getpixel((168,312))==(1,1,1) or im.getpixel((168,312))==(0,2,3):
#         pyautogui.press('j')
#     elif im.getpixel((232,312))==(1,1,1) or im.getpixel((232,312))==(0,2,3):
#         pyautogui.press('k')
#     #im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) +'.png', 'PNG')
#time.sleep(2.4)
# while True:
#     screenGrab()

##dont tape it 

def screenGrab():
    im = ImageGrab.grab((324,228,647,552))
    listpos = [40,120,200,280]
    for i in listpos:
        for j in listpos:
            if im.getpixel((i,j))==(0,0,0):
                pyautogui.click(i+324,228+j)
    
    
time.sleep(2.4)
while True:
    screenGrab()

# while True:
#     print(pyautogui.position())