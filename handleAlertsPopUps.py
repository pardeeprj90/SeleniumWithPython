import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[contains(text(),'Click for JS Prompt')]").click()

alertWindow = driver.switch_to.alert
print(alertWindow.text)
alertWindow.send_keys("Welcome")
# alertWindow.accept()
alertWindow.dismiss()
time.sleep(5)