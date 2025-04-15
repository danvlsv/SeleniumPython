from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)


    browser.find_element(By.CSS_SELECTOR,"[name='firstname']").send_keys('Name')

    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('Last Name')

    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('inbox@mail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"

    file_path = os.path.join(current_dir, file_name)

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)


    submit = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    time.sleep(10)
    browser.quit()