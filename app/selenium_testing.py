import multiprocessing
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from unittest import TestCase

from app import create_app, db
from config import TestConfig

class TestGroupCreation(TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5000')
    
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login(self):
        self.driver.get('http://127.0.0.1:5000/login')
        time.sleep(3)
        username_field = self.driver.find_element("xpath", "//input[@name='username']")
        password_field = self.driver.find_element("xpath", "//input[@name='password']")
        username_field.send_keys("user1")
        password_field.send_keys("password")
        self.driver.execute_script('window.scrollBy(0,240)')
        time.sleep(3)
        submit_button = self.driver.find_element("xpath", "//input[@name='submit']")
        submit_button.click()

    def test_signup(self):
        self.driver.get('http://127.0.0.1:5000/signup')
        username_field = self.driver.find_element("xpath", "//input[@name='username']")
        email_field = self.driver.find_element("xpath", "//input[@name='email']")
        password_field = self.driver.find_element("xpath", "//input[@name='password']")
        password2_field = self.driver.find_element("xpath", "//input[@name='password2']")
        time.sleep(8)
        self.driver.execute_script('window.scrollBy(0,280)')
        time.sleep(3)
        submit_button = self.driver.find_element("xpath", "//input[@name='submit']")

        username_field.send_keys("testuser")
        email_field.send_keys("aviv2silman@gmail.com")
        password_field.send_keys("password64")
        self.driver.execute_script('window.scrollBy(0,190)')
        password2_field.send_keys("password64")
        self.driver.execute_script('window.scrollBy(0,190)')
        submit_button.click()

    def test_create_accountlink(self):
        self.driver.get('http://127.0.0.1:5000/login')
        self.driver.execute_script('window.scrollBy(0,240)')
        link_to_signup = self.driver.find_element("xpath", "//a[@href='/signup']")
        self.driver.execute_script('window.scrollBy(0,240)')
        time.sleep(4)
        link_to_signup.click()

    def test_already_have_account_link(self):
        self.driver.get('http://127.0.0.1:5000/signup')
        self.driver.execute_script('window.scrollBy(0,490)')
        link_to_login = self.driver.find_element("xpath", "//a[@href='/login']")
        self.driver.execute_script('window.scrollBy(0,240)')
        time.sleep(3)
        self.driver.execute_script('window.scrollBy(0,240)')
        link_to_login.click()

    def test_navbar_offer(self):
        self.driver.get('http://127.0.0.1:5000/index')
        time.sleep(2)
        offers = self.driver.find_element("xpath", "//a[@href='/offers']")
        time.sleep(2)
        offers.click()

    def test_navbar_request(self):
        self.driver.get('http://127.0.0.1:5000/offers')
        time.sleep(2)
        requests = self.driver.find_element("xpath", "//a[@href='/requests']")
        time.sleep(2)
        requests.click()

    def test_navbar_profile(self):
        self.driver.get('http://127.0.0.1:5000/requests')
        time.sleep(2)
        home = self.driver.find_element("xpath", "//a[@href='/index']")
        time.sleep(2)
        home.click()










    #def test_alreadyhaveaccountlink(self):
    #    self.driver.get('http://127.0.0.1:5000/signup')
    #    self.driver.execute_script('window.scrollBy(0,240)')
    #    time.sleep(2)
    #    link_to_login = self.driver.find_element("xpath", "//a[@href='/login']")
    #    self.driver.execute_script('window.scrollBy(0,240)')
    #    time.sleep(2)
        #link_to_login.click()
