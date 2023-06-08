from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage


class AppstorePage(BasePage):
    TOPS = (By.TAG_NAME, "data-facet-name = 'Tops'")
    SEARCH = (By.ID, "globalSearchInputField")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL + "gp/mas/get/android")

    def get_appstore_page_title(self, title):
        return self.get_title(title)
