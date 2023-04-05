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

driver.get("https://www.opencart.com/index.php?route=account/register")
time.sleep(2)
countryDropDown = driver.find_element(By.XPATH,"//select[@id='input-country']")
country = Select(countryDropDown)
country.select_by_visible_text("India")