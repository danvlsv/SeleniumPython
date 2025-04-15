from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)


    browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()

    alert = browser.switch_to.alert
    alert.accept()

    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value")
    num1 = int(x_el.text)

    browser.find_element(By.CSS_SELECTOR,"#answer").send_keys(str(calc(int(x_el.text))))
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


finally:
    time.sleep(10)
    browser.quit()