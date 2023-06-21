from selenium.webdriver.common.by import By

from pages.AppstorePage import AppstorePage
from pages.BasePage import BasePage


class MenuPage(BasePage):
    AMAZON_APPSTORE = (By.XPATH, "//*[@id='hmenu-content']//*[contains(text(),'Amazon Appstore')]")
    DOWNLOAD_A_APPSTORE = (By.XPATH, "//*[@id='hmenu-content']//*[contains(text(),'Download Amazon Appstore')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_appstore(self):
        self.do_click(self.AMAZON_APPSTORE)

    def click_download_appstore(self):
        self.do_click(self.DOWNLOAD_A_APPSTORE)
        return AppstorePage(self.driver)
