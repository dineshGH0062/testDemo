
import unittest
import json

from selenium.webdriver import Chrome

from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from selenium.webdriver.common.keys import Keys
from lib.utils import create_drivers


class TestLoginS123(unittest.TestCase):
    def setUp(self):

        self.driver=create_drivers.get_driver_instance()
        #self.driver=Chrome('C:/Users/dinu/PycharmProjects/New_actiTIME/browser_server/chromedriver.exe')
        #self.driver.get("http://localhost")
        #self.driver.implicitly_wait(30)
        #self.driver.maximize_window()
        self.login=LoginPage(self.driver)

        self.home=HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_valid_login_tc132(self):
         data=json.load(open('C:/Users/dinu/PycharmProjects/actiTIME/test/regression/login/test_data.json'))
         self.login.wait_for_login_page_to_load()
         self.login.get_username_textbox().send_keys(data['TC123567']['username'])
         self.login.get_password_textbox().send_keys(data['TC123567']['pwd'])
         # self.login.get_username_textbox().send_keys("admin")
         # self.login.get_password_textbox().send_keys("manager")
         self.login.get_login_button().click()
         self.home.wait_for_home_page_to_load()
         actual_title=self.driver.title
         assert actual_title==data['TC123567']['title']

         print(actual_title)
         #expected_title = 'actiTIME - Enter Time-Track'
         #assert actual_title==expected_title
         self.home.get_logout_button().click()
         self.login.wait_for_login_page_to_load()

