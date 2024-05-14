from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to the chromedriver executable
cService = webdriver.ChromeService(executable_path='app/chromedriver.exe')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service = cService)

# Open Google in the browser
driver.get('http://127.0.0.1:5000')
# Wait for 5 seconds
time.sleep(5)

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

driver.quit()
