from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "ap_email")
    CONTINUE_BUTTON = (By.ID, "continue")
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, "Create your Amazon account")
    PROBLEM_MESSAGE = (By.CLASS_NAME, "a-alert-heading")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_PAGE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username):
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.CONTINUE_BUTTON)

    def is_create_account_link_exist(self):
        return self.is_visible(self.CREATE_ACCOUNT_LINK)

    def is_problem_message(self):
        return self.is_visible(self.PROBLEM_MESSAGE)
