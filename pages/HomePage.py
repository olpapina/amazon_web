from selenium.webdriver.common.by import By

from components.PopUpPage import PopUpPage
from components.SearchBlockPage import SearchBlockPage
from components.SignInPopUpPage import SignInPopUpPage
from config.config import TestData
from pages.BasePage import BasePage
from components.MenuPage import MenuPage
from pages.ChangeLocationPage import ChangeLocationPage


class HomePage(BasePage):
    MENU = (By.ID, "nav-hamburger-menu")
    SIGN_IN_POP_UP = (By.ID, "nav-signin-tooltip")
    POP_UP = (By.ID, "glow-toaster-body")
    DELIVERY_LOCATION_BLOCK = (By.ID, "glow-ingress-block")
    DELIVERY_LOCATION_ICON = (By.ID, "nav-packard-glow-loc-icon")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_menu(self):
        self.do_click(self.MENU)
        return MenuPage(self.driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_sign_in_visible(self):
        flag = self.is_visible(self.SIGN_IN_POP_UP)
        assert flag

    def get_pop_up(self):
        return PopUpPage(self.driver)

    def get_search_block(self):
        return SearchBlockPage(self.driver)

    def get_sign_in(self):
        return SignInPopUpPage(self.driver)

    def get_delivery_location_text(self):
        return self.get_element_text(self.DELIVERY_LOCATION_BLOCK)

    def click_change_location(self):
        self.do_click(self.DELIVERY_LOCATION_ICON)
        return ChangeLocationPage(self.driver)
