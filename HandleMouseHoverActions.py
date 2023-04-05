import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
userName = driver.find_element(By.XPATH, "//input[@name='username']")
userName.clear()
userName.send_keys("Admin")

userPassword = driver.find_element(By.XPATH, "//input[@name='password']")
userPassword.clear()
userPassword.send_keys("admin123")

submitBtn = driver.find_element(By.XPATH, "//button[@type='submit']")
submitBtn.click()