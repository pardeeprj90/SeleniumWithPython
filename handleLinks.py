import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/")
# driver.find_element(By.LINK_TEXT,'Digital downloads').click()
# Find total links in webpage
# links = driver.find_elements(By.TAG_NAME,'a')
# print(f'Number of available links in webpage are {len(links)}')
# for link in links:
#     print(link.text)
# time.sleep(5)

driver.get("http://www.deadlinkcity.com/")
links = driver.find_elements(By.TAG_NAME,'a')
count =0
for link in links:
    url = link.get_attribute('href')
    res = requests.head(url)
    if res.status_code>=400:
        print(f'{url} is a broken link')
        count+=1