import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

# Set the path to the chromedriver executable
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)

driver.get('http://127.0.0.1:5000')
driver.maximize_window()

time.sleep(5)
driver.execute_script('window.scrollBy(0,240)')
link_to_signup = driver.find_element("xpath", "//a[@href='/signup']")
driver.execute_script('window.scrollBy(0,240)')
time.sleep(8)
link_to_signup.click()

username_field = driver.find_element("xpath", "//input[@name='username']")
email_field = driver.find_element("xpath", "//input[@name='email']")
password_field = driver.find_element("xpath", "//input[@name='password']")
password2_field = driver.find_element("xpath", "//input[@name='password2']")
time.sleep(8)
driver.execute_script('window.scrollBy(0,280)')
time.sleep(3)
submit_button = driver.find_element("xpath", "//input[@name='submit']")

username_field.send_keys("testuser")
email_field.send_keys("aviv2silman@gmail.com")
password_field.send_keys("password64")
driver.execute_script('window.scrollBy(0,190)')
password2_field.send_keys("password64")
driver.execute_script('window.scrollBy(0,190)')
submit_button.click()

time.sleep(3)
username_field = driver.find_element("xpath", "//input[@name='username']")
password_field = driver.find_element("xpath", "//input[@name='password']")
username_field.send_keys("testuser")
password_field.send_keys("password64")
driver.execute_script('window.scrollBy(0,240)')
time.sleep(3)
submit_button = driver.find_element("xpath", "//input[@name='submit']")
submit_button.click()

time.sleep(6)
offers = driver.find_element("xpath", "//a[@href='/offers']")
offers.click()

time.sleep(2)
requests = driver.find_element("xpath", "//a[@href='/requests']")
requests.click()

time.sleep(2)
home = driver.find_element("xpath", "//a[@href='/index']")
home.click()

time.sleep(2)
logout = driver.find_element("xpath", "//a[@href='/logout']")
logout.click()