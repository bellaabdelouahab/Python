import webbrowser
import pyautogui
import time


person_name = input('Enter The Person Name Whom You Want To Send A Message: ')
my_msg = input('Enter Your Message: ')

#webbrowser.open('https://web.whatsapp.com/')

time.sleep(1)
print(pyautogui.position())

# click on search bar
pyautogui.click(184,189)
pyautogui.typewrite(person_name)


time.sleep(1)

#click on person 
pyautogui.click(163,319)

time.sleep(1)

pyautogui.typewrite(my_msg)

time.sleep(1)
pyautogui.click(1332,692) # click on Send button

