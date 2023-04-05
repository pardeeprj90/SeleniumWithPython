import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)