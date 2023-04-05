import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://text-compare.com/")
input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("Test")
act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)
