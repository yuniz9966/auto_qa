import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_text_input(driver):
    driver.get("http://uitestingplayground.com/textinput")
    wait = WebDriverWait(driver, 15)
    text_field = driver.find_element(By.XPATH, "//input[@class='form-control']")
    text_field.click()
    text_field.send_keys("ITCH")
    execute_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    execute_button.click()

    execute_button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='btn btn-primary']" )
        )
    )
    assert execute_button, "ТЕСТ НЕ ПРОШЕЛ"


def test_check_image(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    time.sleep(10)
    image_locator = driver.find_element(By.XPATH, '//img[@alt="award"]')
    assert image_locator.get_attribute("alt") == "award"
