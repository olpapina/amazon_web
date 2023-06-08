from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class PopUpPage(BasePage):
    POP_UP = (By.ID, "glow-toaster-body")
    BUTTON_CHANGE_ADDRESS = (By.CLASS_NAME, "glow-toaster-button-submit")
    BUTTON_DONT_CHANGE = (By.CLASS_NAME, "glow-toaster-button-dismiss")

    def __init__(self, driver):
        super().__init__(driver)

    def click_dont_change(self):
        self.do_click(self.BUTTON_DONT_CHANGE)
