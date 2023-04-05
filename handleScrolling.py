import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# Vertical Scroll approach 1
# driver.execute_script("window.scrollBy(0,3000)","")
# pixels = driver.execute_script("return window.pageYOffset;")
# print(pixels)

# Vertical Scroll approach 2
# flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# pixels = driver.execute_script("return window.pageYOffset;")
# print(pixels)

# Vertical Scroll approach 3 scroll till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
pixels = driver.execute_script("return window.pageYOffset;")
print(pixels)
time.sleep(5)