import unittest
from lib.ui.login_page import LoginPage
from lib.utils import create_drivers


class TestComponets(unittest.TesCase):
    def setUp(self):
        self.driver=create_drivers.get_driver_instance()

        self.login=LoginPage(self.driver)


    def tearDown(self):
        self.driver.close()


    def test_framework_components(self):
        self.login.wait_for_login_page_to_load()
        actual_title=self.driver.title
        expected_title='actiTIME - Login'
        assert actual_title==expected_title,'Dint match error msg'
