import unittest
from selenium.webdriver import Chrome
from selenium import webdriver

from lib.ui.login_page import LoginPage
from lib import create_driver


class TestComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/dinu/Downloads/browser/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost")

        self.login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def wait_for_login_page_to_load(self):
        self.login.wait_for_login_page_to_load()
        #actaul_title = self.driver.title
        #expected_title = 'actiTIME - Login'
        #assert actaul_title == expected_title, 'Title is not matching'