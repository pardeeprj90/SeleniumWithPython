from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create an instance of the WebDriver for your browser with desired options
options = Options()
options.add_argument("--disable-notifications")  # Disable notifications

service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
driver.maximize_window()
driver.get("https://whatmylocation.com/")