from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

receiver = str(input('Enter name of Person:'))

message = str(input('Enter your message: '))

count = int(input('Number of times you need to send the message: '))

driver = webdriver.Chrome(r"your complete path for chrome drive ")
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
x_arg = '//span[contains(@title, '+ '"' +receiver + '"'+ ')]'
#print(x_arg)
person_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
#print(person_title)
person_title.click()
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

for i in range(count):
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(1)