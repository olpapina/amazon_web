from config.config import TestData
from pages.HomePage import HomePage
from tests.test_base import BaseTest


class Test_HomePage(BaseTest):

    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_sign_in_visible(self):
        self.homePage = HomePage(self.driver)
        self.homePage.is_sign_in_visible()

    # def test_click_menu(self):
    #     self.homePage = HomePage(self.driver)
    #     self.homePage.click_menu()

    def test_search(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_search_type()

