import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
# day = driver.find_element(By.ID,"monday")
# day.click()
days = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
for day in days:
    day.click()
time.sleep(5)