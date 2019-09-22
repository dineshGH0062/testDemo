from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OpenTaskPage:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_open_task_page_to_load(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_add__new_task_button()))

    def get_add__new_task_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@value='Create New Tasks']")
        except:
            return None

    def get_creation_msg(self,index=1):
        xpath_exp="(//span[@class='successmsg'])("+ str(index)+")"
        try:
            return self.driver.find_element_by_xpath(xpath_exp)
        except:
            return None
