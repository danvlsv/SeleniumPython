from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)


    book_button = browser.find_element(By.CSS_SELECTOR,'#book')

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button.click()

    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value")
    num1 = int(x_el.text)

    browser.find_element(By.CSS_SELECTOR,"#answer").send_keys(str(calc(int(x_el.text))))
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


finally:
    time.sleep(10)
    browser.quit()