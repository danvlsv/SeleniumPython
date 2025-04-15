from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder*='your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder*='your last name']")
    input2.send_keys("Truha")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder*='your email']")
    input3.send_keys("Petrov@gmail.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "[placeholder*='your phone']")
    input4.send_keys("7922")
    input5 = browser.find_element(By.CSS_SELECTOR, "[placeholder*='your address']")
    input5.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(5)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()