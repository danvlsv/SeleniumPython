from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration1_should_pass(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        try:
            # Используем уникальные селекторы для обязательных полей
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
            input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
            input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')

            input1.send_keys("Ivan")
            input2.send_keys("Petrov")
            input3.send_keys("email@example.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text = browser.find_element(By.TAG_NAME, "h1").text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            browser.quit()

    def test_registration2_should_fail(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        try:
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
            input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
            input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')

            input1.send_keys("Ivan")
            input2.send_keys("Petrov")
            input3.send_keys("email@example.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text = browser.find_element(By.TAG_NAME, "h1").text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()
