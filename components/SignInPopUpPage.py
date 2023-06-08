from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage


class SignInPopUpPage(BasePage):
    SIGN_IN_BUTTON = (By.XPATH, "//*[@id='nav-signin-tooltip']//*[contains(text(),'Sign in')]")
    SIGN_IN_POP_UP = (By.ID, "nav-signin-tooltip")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in(self):
        self.do_click(self.SIGN_IN_BUTTON)
        return LoginPage(self.driver)
