from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://google.com')
elem = driver.find_element(By.XPATH,'//*[@id="lst-ib"]')
time.sleep(2)
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)
time.sleep(3)
driver.refresh()