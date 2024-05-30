import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://github.com/login")
    time.sleep(3)
    login_elem = driver.find_element(By.ID, "login_field")
    login_elem.send_keys("dgdfgdfgdgdfgdfg@gmail.com")
    time.sleep(3)
    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("12345678")
    time.sleep(3)
    driver.find_element(By.NAME, "commit").click()
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(5)
    driver.close()
