# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
#
#
#
# web_driver = webdriver.Chrome()
# web_driver.get("https://suninjuly.github.io/cats.html")
#
# try:
#     elements = web_driver.find_element(By.ID, "login-button")
# except NoSuchElementException as err:
#     print(f"Ошибка: {err}")
#
#
# print(elements)