import multiprocessing
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

from app import create_app, db
from config import TestConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

    def login(self):
        logger.info('Logging in')
        self.driver.get('http://127.0.0.1:5000/login')
        username_field = self.driver.find_element(By.XPATH, "//input[@name='username']")
        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        username_field.send_keys("user1")
        password_field.send_keys("password")
        self.driver.execute_script('window.scrollBy(0,240)')
        submit_button = self.driver.find_element(By.XPATH, "//input[@name='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)  # JavaScript click
        logger.info('Logged in successfully')

    def test_login(self):
        logger.info('Starting test_login')
        self.login()
        logger.info('Finished test_login')

    def test_signup(self):
        logger.info('Starting test_signup')
        self.driver.get('http://127.0.0.1:5000/signup')
        username_field = self.driver.find_element(By.XPATH, "//input[@name='username']")
        email_field = self.driver.find_element(By.XPATH, "//input[@name='email']")
        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password2_field = self.driver.find_element(By.XPATH, "//input[@name='password2']")
        self.driver.execute_script('window.scrollBy(0,280)')
        submit_button = self.driver.find_element(By.XPATH, "//input[@name='submit']")

        username_field.send_keys("testuser")
        email_field.send_keys("aviv2silman@gmail.com")
        password_field.send_keys("password64")
        self.driver.execute_script('window.scrollBy(0,190)')
        password2_field.send_keys("password64")
        self.driver.execute_script('window.scrollBy(0,190)')
        self.driver.execute_script("arguments[0].click();", submit_button)  # JavaScript click
        logger.info('Finished test_signup')

    def test_create_accountlink(self):
        logger.info('Starting test_create_accountlink')
        self.driver.get('http://127.0.0.1:5000/login')
        link_to_signup = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/signup']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link_to_signup)
        self.driver.execute_script("arguments[0].click();", link_to_signup)  # JavaScript click
        logger.info('Finished test_create_accountlink')

    def test_already_have_account_link(self):
        logger.info('Starting test_already_have_account_link')
        self.driver.get('http://127.0.0.1:5000/signup')
        link_to_login = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link_to_login)
        self.driver.execute_script("arguments[0].click();", link_to_login)  # JavaScript click
        logger.info('Finished test_already_have_account_link')

    def test_navbar_offer(self):
        logger.info('Starting test_navbar_offer')
        self.login()
        self.driver.get('http://127.0.0.1:5000/index')
        offers = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/offers']"))
        )
        self.driver.execute_script("arguments[0].click();", offers)  # JavaScript click
        logger.info('Finished test_navbar_offer')

    def test_navbar_request(self):
        logger.info('Starting test_navbar_request')
        self.login()
        self.driver.get('http://127.0.0.1:5000/offers')
        requests = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/requests']"))
        )
        self.driver.execute_script("arguments[0].click();", requests)  # JavaScript click
        logger.info('Finished test_navbar_request')

    def test_navbar_profile(self):
        logger.info('Starting test_navbar_profile')
        self.login()
        self.driver.get('http://127.0.0.1:5000/requests')
        home = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/index']"))
        )
        self.driver.execute_script("arguments[0].click();", home)  # JavaScript click
        logger.info('Finished test_navbar_profile')