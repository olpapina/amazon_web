from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "ap_email")
    CONTINUE_BUTTON = (By.ID, "continue")
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, "Create your Amazon account")
    PROBLEM_MESSAGE = (By.CLASS_NAME, "a-alert-heading")
    REASON_OF_PROBLEM = (By.CLASS_NAME, "a-list-item")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username):
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.CONTINUE_BUTTON)

    def is_create_account_link_exist(self):
        return self.is_visible(self.CREATE_ACCOUNT_LINK)

    def is_problem_message(self):
        return self.is_visible(self.PROBLEM_MESSAGE)

    def get_problem_message_text(self):
        return self.get_element_text(self.PROBLEM_MESSAGE)

    def get_problem_message_reason(self):
        return self.get_element_text(self.REASON_OF_PROBLEM)
