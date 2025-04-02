# from selenium.webdriver.common.by import By
# import time
# import pytest
# from selenium import webdriver
#
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
#
#
# def test_1(driver):
#     driver.get("https://suninjuly.github.io/cats.html")
#     element = driver.find_element(By.TAG_NAME, "h1")
#     assert element.text == "Cat memes", "тест не прошел"
#
#
# # Написать тест, который проверяет наличия текста "9 mins" в значении времени карточки номер 1
# def test_2(driver):
#     driver.get("https://suninjuly.github.io/cats.html")
#     elements = driver.find_elements(By.XPATH, "//*[@class='text-muted']")
#     print(elements[1].text)
#     assert elements[1].text == "9 mins", "тест не прошел"
#
#
# # Написать тест, который проверяет наличия теста "I love you so much" в названии последней карточки
# def test_3(driver):
#     driver.get("https://suninjuly.github.io/cats.html")
#     element = driver.find_element(By.XPATH, "//*[text()='I love you so much']")
#     assert element, "тест не прошел"
#
#
# # Написать тест, который проверяет наличия теста "Cats album"  возле иконки фото
# def test_find_CatsAlbum(driver):
#     driver.get("https://suninjuly.github.io/cats.html")
#     time.sleep(3)
#     element = driver.find_element(By.XPATH, "//*[@class='navbar-brand d-flex align-items-center']")
#     new = element.find_element(By.TAG_NAME, "svg")
#     new2 = element.find_element(By.XPATH, "//*[contains(text(),'Cats album')]").text
#     assert element
#     assert new
#     assert new2