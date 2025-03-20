# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://github.com/yuniz9966?tab=repositories")
# # driver.save_screenshot('./screens/1.png')
# about_link = driver.find_element(By.LINK_TEXT, "Stars")
# about_link.click()
#
# time.sleep(3)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://itcareerhub.de/ru")
about_link = driver.find_element(By.LINK_TEXT, 'О нас')
about_link.click()
time.sleep(5)
driver.quit()
