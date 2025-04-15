from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_ = x_element.text
    print(x_)
    y = calc(x_)

    answer = browser.find_element(By.CSS_SELECTOR,"#answer")
    answer.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()


    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()


    submit = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()