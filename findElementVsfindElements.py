import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

# find_element() returns only signle webelement

searchInputBox_ele = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
searchInputBox_ele.send_keys("Apple Macbook Pro 13-inch")
time.sleep(4)

# When locator is matching with multiple webelement