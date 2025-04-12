import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import os
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

#
#
# def test_fill_form_and_check_alert(browser):
#     browser.get('http://suninjuly.github.io/huge_form.html')
#     input_fields = browser.find_elements(By.TAG_NAME, 'input')
#     for field in input_fields:
#         field.clear()
#         field.send_keys('Hello')
#
#     submit_btn = browser.find_element(By.CLASS_NAME, 'btn-default')
#     submit_btn.click()
#
#     wait = WebDriverWait(browser, 10)
#     alert = wait.until(EC.alert_is_present())
#
#     alert_text = Alert(browser).text
#
#     expected_substring = "Congrats, you've passed the task!"
#
#     assert expected_substring in alert_text, 'стока не найдена'
#
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#
# def test_math_form(browser):
#     browser.get("https://suninjuly.github.io/math.html")
#     x_value = browser.find_element(By.ID, "input_value").text
#     result = calc(x_value)
#     answer = browser.find_element(By.ID, "answer")
#     answer.send_keys(result)
#
#     robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
#     robot_checkbox.click()
#
#     radio_button = browser.find_element(By.ID, "robotsRule")
#     radio_button.click()
#
#     submit_btn = browser.find_element(By.CLASS_NAME, 'btn-default')
#     submit_btn.click()
#
#     wait = WebDriverWait(browser, 10)
#     alert = wait.until(EC.alert_is_present())
#     alert_text = Alert(browser).text
#
#     expected_substring = "Congrats, you've passed the task!"
#
#     assert expected_substring in alert_text, 'стока не найдена'
#     alert.accept()
#     time.sleep(3)

#
# def test_fill_upload(browser):
#     browser.get("http://suninjuly.github.io/file_input.html")
#
#     browser.find_element(By.NAME, "firstname").send_keys("John")
#     browser.find_element(By.NAME, "lastname").send_keys("Doe")
#     browser.find_element(By.NAME, "email").send_keys("test@example.com")
#
#     file_path = os.path.abspath('test_file.txt')
#     with open(file_path, 'w') as f:
#         f.write('привет я новый файл')
#
#     file_input = browser.find_element(By.ID, 'file')
#     file_input.send_keys(file_path)
#
#     submit_btn = browser.find_element(By.CLASS_NAME, 'btn-primary')
#     submit_btn.click()
#
#     wait = WebDriverWait(browser, 10)
#
#     alert = wait.until(EC.alert_is_present())
#
#     alert_text = Alert(browser).text
#     expected_substring = "Congrats, you've passed the task!"
#     assert expected_substring in alert_text, 'стока не найдена'
#     alert.accept()
#     os.remove(file_path)
#     time.sleep(3)


# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://example.com")
#
# # Открываем новую вкладку
# driver.execute_script("window.open('https://google.com', '_blank');")
#
# # Выводим список всех вкладок
# print(driver.window_handles)
#
#
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# import  time
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://www.iana.org/help/example-domains")
#
# element_to_hover = driver.find_element(By.LINK_TEXT, 'Domains')
#
# actions = ActionChains(driver)
# actions.move_to_element(element_to_hover).perform()
# time.sleep(3)
