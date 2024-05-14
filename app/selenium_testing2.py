import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

# Set the path to the chromedriver executable
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)

driver.get('http://127.0.0.1:5000)

