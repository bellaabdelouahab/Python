import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:/Program Files/Tesseract-OCR/tesseract.exe"
from PIL import ImageGrab
import pyautogui
import time
import os

# while True:
#     print(pyautogui.position())
def screenGrab():
    im = ImageGrab.grab((488,623,599,657))
    # im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) +'.png', 'PNG')
    return im



# img = cv2.imread("C:/Users/Abdelouahab/Pictures/DataBaseModule/2_1.png")
while True:
    time.sleep(5)
    text = pytesseract.image_to_string(screenGrab())
    try:
        nbr = int(text[0:3])
    except:
        print("Invalid\n",text)
        nbr=False
    if nbr:
        pyautogui.write(str(nbr+1))
        pyautogui.press("ENTER")