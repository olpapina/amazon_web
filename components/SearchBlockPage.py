from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage
from pages.ResultPage import ResultPage


class SearchBlockPage(BasePage):
    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        super().__init__(driver)

    def do_search(self):
        self.do_send_keys(self.SEARCH, TestData.SEARCH_TEXT)
        self.do_click(self.SEARCH_BUTTON)
        return ResultPage(self.driver)
