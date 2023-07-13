from config.config import TestData
from pages.HomePage import HomePage
from tests.test_base import BaseTest


class TestHomePage(BaseTest):

    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_sign_in_visible(self):
        self.homePage = HomePage(self.driver)
        self.homePage.is_sign_in_visible()

    def test_delivery_location(self):
        self.homePage = HomePage(self.driver)
        text = self.homePage.get_delivery_location_text()
        assert TestData.ACTUAL_DELIVERY_LOCATION in text

    def test_change_delivery_location(self):
        self.homePage = HomePage(self.driver)
        self.changeLocationPage = self.homePage.click_change_location()
        self.changeLocationPage.select_location()
        self.homePage = HomePage(self.driver)
        text = self.homePage.get_delivery_location_text()
        assert TestData.CHANGED_LOCATION in text
