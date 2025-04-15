from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    num1_el = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = int(num1_el.text)


    num2_el = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = int(num2_el.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num1+num2))


    submit = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()