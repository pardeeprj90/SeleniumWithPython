import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://www.google.com")
driver.back()
time.sleep(3)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)

driver.quit()
time.sleep(3)