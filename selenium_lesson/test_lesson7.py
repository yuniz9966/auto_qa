import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_success_login_valid_data(driver):
    user_name_input_field = driver.find_element(By.ID, 'user-name')
    user_name_input_field.send_keys('standard_user')
    user_name_input_field = driver.find_element(By.ID, 'password')
    user_name_input_field.send_keys('secret_sauce')
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    inventory_list = driver.find_element(By.CLASS_NAME, 'inventory_list')
    assert inventory_list, 'мписок товаров не отображается'


def test_succsefull_enter_password(driver):
    user_name_input_field = driver.find_element(By.ID, 'user-name')
    user_name_input_field.send_keys('standard_user')
    user_name_input_field = driver.find_element(By.ID, 'password')
    user_name_input_field.send_keys('secret_sauce_123')
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    time.sleep(5)
    error_massage = driver.find_element(By.CLASS_NAME, 'error-message-container')
    assert "Username and password do not match" in error_massage.text