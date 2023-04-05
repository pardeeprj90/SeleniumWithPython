import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")
searchBox = driver.find_element(By.NAME,'q')
searchBox.send_keys("Selenium")
searchBox.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()