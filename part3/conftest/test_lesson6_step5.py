import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import json

links = [
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'
]

@pytest.fixture(scope="session")
def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config

@pytest.mark.parametrize('link',links)
def test_submit_answer(browser,link,load_config):
    browser.get(f"{link}")
    browser.implicitly_wait(10)

    WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CLASS_NAME,"navbar__auth_login")))
    browser.find_element(By.CLASS_NAME,"navbar__auth_login").click()

    browser.find_element(By.ID,"id_login_email").send_keys(load_config['login_stepik'])

    browser.find_element(By.ID,"id_login_password").send_keys(load_config['password_stepik'])

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    WebDriverWait(browser,12).until(EC.invisibility_of_element((By.CLASS_NAME,'modal-dialog')))

    browser.implicitly_wait(10)

    WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
    textarea=browser.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(str(math.log(int(time.time()))))

    WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    browser.find_element(By.CLASS_NAME, "submit-submission").click()

    browser.implicitly_wait(10)
    WebDriverWait(browser,12).until(EC.visibility_of_element_located((By.CLASS_NAME,"smart-hints__hint")))
    result = browser.find_element(By.CLASS_NAME,"smart-hints__hint").text

    assert result=="Correct!", result

    WebDriverWait(browser,5)
    WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CLASS_NAME, 'again-btn'))).click()
