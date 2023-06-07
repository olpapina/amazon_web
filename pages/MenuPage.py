from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage


class MenuPage(BasePage):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver.get(TestData.BASE_URL)

    def click_appstore(self):
        self.do_click(self.AMAZON_APPSTORE)
