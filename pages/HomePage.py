from selenium.webdriver.common.by import By
from config.config import TestData
from pages.AppstorePage import AppstorePage
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.MenuPage import MenuPage

class HomePage(BasePage):
    SIGN_IN_BUTTON = (By.XPATH, "//*[@id='nav-signin-tooltip']//*[contains(text(),'Sign in')]")
    SIGN_IN_POP_UP = (By.ID, "nav-signin-tooltip")
    POP_UP = (By.ID, "glow-toaster-body")
    BUTTON_CHANGE_ADDRESS = (By.CLASS_NAME, "glow-toaster-button-submit")
    BUTTON_DONT_CHANGE = (By.CLASS_NAME, "glow-toaster-button-dismiss")
    MENU = (By.ID, "nav-hamburger-menu")
    AMAZON_APPSTORE = (By.XPATH, "//*[@id='hmenu-content']//*[contains(text(),'Amazon Appstore')]")
    SEARCH = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    DOWNLOAD_A_APPSTORE = (By.XPATH, "//*[@id='hmenu-content']//*[contains(text(),'Download Amazon Appstore')]")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_menu(self):
        self.do_click(self.MENU)
        return MenuPage(self.driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def do_search_type(self):
        self.do_send_keys(self.SEARCH, "iPhone")

    def is_sign_in_visible(self):
        flag = self.is_visible(self.SIGN_IN_POP_UP)
        assert flag

    def click_appstore(self):
        self.do_click(self.AMAZON_APPSTORE)

    def click_download_appstore(self):
        self.do_click(self.DOWNLOAD_A_APPSTORE)
        return AppstorePage(self.driver)

    def click_sign_in(self):
        self.do_click(self.SIGN_IN_BUTTON)
        return LoginPage(self.driver)

    def click_dont_change(self):
        self.do_click(self.BUTTON_DONT_CHANGE)