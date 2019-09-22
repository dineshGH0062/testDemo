import json
import unittest

from lib.ui.add_new_task_page import AddNewTaskPage
from lib.ui.home_page import HomePage
from lib.ui.login_page import LoginPage
from lib.ui.open_task_page import OpenTaskPage
from lib.utils import create_drivers


class CreateTaskU15632(unittest.TestCase):
    def setUp(self):
        self.driver=create_drivers.get_driver_instance()
        self.login=LoginPage(self.driver)
        self.home=HomePage(self.driver)
        self.open_task=OpenTaskPage(self.driver)
        self.add_task=AddNewTaskPage(self.driver)


    def tearDown(self):
        self.driver.close()

    def test_create_taskTC132576(self):
        data=json.load(open("C:/Users/dinu/PycharmProjects/actiTIME/test/regression/login/test_data.json"))
        self.login.wait_for_login_page_to_load()
        self.login.get_username_textbox().send_keys(data['TC123567']['username'])
        self.login.get_password_textbox().send_keys(data['TC123567']['pwd'])
        self.login.get_login_button().click()
        self.open_task.wait_for_open_task_page_to_load()
        self.open_task.get_add__new_task_button().click()
        self.add_task.wait_for_add_new_task_page_to_load()
        self.add_task.select_customer()
        self.add_task.get_customer_textbox().send_keys(data['TC132576']['cName'])
        self.add_task.get_project_textbox().send_keys(data['TC132576']['project'])
        self.add_task.get_task_textbox().send_keys(data['TC132576']['task'])

        self.add_task.get_create_task_button().click()

        self.open_task.wait_for_open_task_page_to_load()

        customer_msg=self.open_task.get_creation_msg(1).text
        assert data['TC132576']['cName'] in customer_msg
        project_msg=self.open_task.get_creation_msg(2).text
        assert data['TC132576']['project'] in project_msg
        task_msg=self.open_task.get_creation_msg(3).text
        assert data['TC132576']['cName'] in task_msg
        assert data['TC132576']['project'] in task_msg

        self.home.get_logout_button().click()
        self.login.wait_for_login_page_to_load()
