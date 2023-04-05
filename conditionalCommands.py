import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

# is_displayed is_enabled
userName = driver.find_element(By.XPATH,"//input[@name='username']")
print(userName.is_displayed())
print(userName.is_enabled())