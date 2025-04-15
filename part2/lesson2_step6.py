from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value")
    num1 = int(x_el.text)

    browser.find_element(By.CSS_SELECTOR,"#answer").send_keys(str(calc(int(x_el.text))))

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()


    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()


    submit = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    time.sleep(10)
    browser.quit()