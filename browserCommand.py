import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(2)
print(driver.current_url)
driver.close()
time.sleep(5)

