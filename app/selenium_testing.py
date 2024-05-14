from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path to the chromedriver executable
cService = webdriver.ChromeService(executable_path='app/chromedriver.exe')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service = cService)

# Open Google in the browser
driver.get('https://www.google.com')

# Find the search input element and enter a random search query
search_input = driver.find_element_by_name('q')
search_input.send_keys('random search query')

# Press Enter to perform the search
search_input.send_keys(Keys.ENTER)

# Close the browser
driver.quit()