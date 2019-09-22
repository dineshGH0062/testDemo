from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddNewTaskPage:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_add_new_task_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_customer_textbox()))

    def select_customer(self,name='--new customer --'):
        status=False
        ddl=self.driver.find_element_by_name("customerID")
        sct=Select(ddl)
        all_options=sct.options
        for option in all_options:
            text=option.text
            if text==name:
                sct.select_by_visible_text(name)
                status=True
                break

        if status==False:
            sct.select_by_visible_text("--new customer --")


    def select_project(self,name='-- new project --'):
        status=False
        ddl=self.driver.find_element_by_name("projectID")
        sct=Select(ddl)
        all_options=sct.options
        for option in all_options:
            text=option.text
            if text==name:
                sct.select_by_visible_text(name)
                status=True
                break
            if status==False:
                sct.select_by_visible_text("-- new project --")

    def get_customer_textbox(self):
        try:
            return self.driver.find_element_by_name("customerName")
        except:
            return None

    def get_project_textbox(self):
        try:
            return self.driver.find_element_by_name("projectName")
        except:
            None

    def get_task_textbox(self):
        try:
            return self.driver.find_element_by_name("task[0].name")
        except:
            return None

    def get_create_task_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@value='Create Tasks']")
        except:
            return None

