import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# By ID
# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# By Link Text & Partial Link Text
# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Regis").click()
# links = driver.find_elements(By.TAG_NAME,"a")
# linkCount = len(links)
# print(linkCount)
# for link in links:
#     if link.text== 'RSS':
#         break
#         print(link.text)
# time.sleep(5)

# CSS Selectors
# Tag id :->> tagname#valueofID
# tag class, tag attribute, tag class attribute